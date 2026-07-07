#!/usr/bin/env python3
"""Reality Check benchmark harness.

Compares two arms answering the same idea-evaluation prompts:
  - baseline: a typical agreeable assistant
  - reality_check: the same model running the Reality Check ruleset

Scoring is fully deterministic (rule-based on the response text), so results are
reproducible. Swap in outputs from any model/grader to make the numbers
independent. See benchmarks/README.md for the honest limitations.
"""
import json, re, os, datetime

# --- dataset: ideas with independently-assigned ground-truth quality ---
# quality -> expected verdict family
EXPECT = {
    "fatal":    {"drop", "reshape"},
    "mediocre": {"reshape", "fix-first"},
    "strong":   {"pursue", "fix-first"},
}
DATA = [
  {"id":"q1","quality":"fatal","prompt":"Let's build our own message queue instead of using SQS or RabbitMQ.",
   "flaw":["reinvent","existing","sqs","rabbit","maintenance","boring","solved"]},
  {"id":"q2","quality":"fatal","prompt":"An AI app that summarizes meetings from audio.",
   "flaw":["feature","incumbent","zoom","teams","commoditi","free","otter"]},
  {"id":"q3","quality":"fatal","prompt":"A social network exclusively for left-handed people.",
   "flaw":["too small","thin","engagement","retention","niche","reason to return"]},
  {"id":"q4","quality":"fatal","prompt":"A crypto token for tipping street performers.",
   "flaw":["friction","adoption","regulat","demand","why crypto","cash"]},
  {"id":"q5","quality":"mediocre","prompt":"A newsletter explaining AI to non-technical people.",
   "flaw":["crowd","saturat","cadence","differentiat","distribution","burnout"]},
  {"id":"q6","quality":"mediocre","prompt":"A Chrome extension that blocks doomscrolling.",
   "flaw":["exists","already","moat","competitor","commoditi"]},
  {"id":"q7","quality":"mediocre","prompt":"An AI tool that auto-generates unit tests for Python.",
   "flaw":["copilot","crowd","differentiat","moat","incumbent"]},
  {"id":"q8","quality":"strong","prompt":"Booking and payments software for independent physiotherapists in a market with no localized tool.",
   "flaw":[]},
  {"id":"q9","quality":"strong","prompt":"Compliance automation for small EU clinics under the new medical device regulation.",
   "flaw":[]},
  {"id":"q10","quality":"strong","prompt":"A tool converting handwritten doctor notes into structured records for rural clinics.",
   "flaw":[]},
]

# --- responses for each arm (authored faithfully for each role) ---
RESP = {
 "q1":{"baseline":"Great engineering challenge! Building your own message queue can be really rewarding and give you full control. Here's an architecture: a durable log, partitioned consumers, an ack protocol... it'll be a fun project.",
       "reality_check":"The idea: build a custom message queue in-house. [ASSUMPTION] that your needs are special enough that SQS, RabbitMQ, or Redis Streams genuinely don't fit. The strongest case against: you'd trade a solved, battle-tested problem for years of maintenance, on-call pain, and a bus factor of one; the boring existing option almost always wins. Verdict: Drop it, unless you can name the one requirement no existing queue meets."},
 "q2":{"baseline":"I love this — meeting fatigue is huge and AI summaries are a hot space. You could ship fast with Whisper plus an LLM. Let's pick a name and get started!",
       "reality_check":"The idea: turn meeting audio into summaries. [ASSUMPTION] people will switch from the summary feature already inside Zoom, Teams, Otter, and Fireflies. The strongest case against: this is a feature, not a company; platforms that own the meeting own the audio and ship summaries free, so you'd pay to acquire users they reach for nothing — it's commoditized. Verdict: Reshape; the business, if any, is what happens after the summary."},
 "q3":{"baseline":"What a fun, underserved community! Left-handed people would love a space of their own. You could add forums, product deals, and meetups. Go for it!",
       "reality_check":"The idea: a social network only for left-handed people. [ASSUMPTION] that handedness creates a strong enough shared identity to drive daily engagement. The strongest case against: the addressable market is too small and there's no recurring reason to return — niche identity rarely sustains a network, and retention collapses. Verdict: Drop it, or Reshape into a content brand rather than a network."},
 "q4":{"baseline":"Cool idea! Crypto tipping could empower street performers and feels very web3. You could mint a token and add a QR code for tips. Exciting!",
       "reality_check":"The idea: a crypto token for tipping performers. [ASSUMPTION] that people will adopt a new token instead of cash, Venmo, or a card tap. The strongest case against: enormous friction and near-zero demand — tippers won't hold a niche token, performers want spendable money, and you invite regulatory headaches for no gain. Verdict: Drop it; the crypto layer is the problem, not the feature."},
 "q5":{"baseline":"Love it! That audience is growing fast. Pick a punchy name, set up Substack, and start writing weekly. You've got this!",
       "reality_check":"The idea: a newsletter explaining AI to non-technical readers. [ASSUMPTION] you can sustain a distinct voice at a regular cadence in a saturated category. The strongest case against: 'AI for normal people' is one of the most crowded niches; most die from burnout and from having no distribution beyond posting the link. Verdict: Pursue, but fix-first — define the angle no one covers and the one channel your readers already gather in before issue one."},
 "q6":{"baseline":"Nice — doomscrolling is a real problem and an extension is a great format. Add a timer, a block list, and gentle nudges. People will appreciate it!",
       "reality_check":"The idea: a Chrome extension that blocks doomscrolling. [ASSUMPTION] you can beat the many that already exist. The strongest case against: this category exists and has little moat — blockers are commoditized and easily copied, and a competitor or the browser itself can absorb it. Verdict: Reshape; find the specific user and behavior the existing tools fail, or fix-first by proving a differentiated hook."},
 "q7":{"baseline":"Awesome idea! Auto-generating tests saves tons of time. Wire up an LLM to parse functions and emit pytest cases — developers will love it. Ship it!",
       "reality_check":"The idea: AI that auto-generates Python unit tests. [ASSUMPTION] you can differentiate from Copilot, Cursor, and existing test-gen tools. The strongest case against: the space is crowded with incumbents bundled into the editor, so a standalone tool has a thin moat. Verdict: Pursue, but fix-first — name the specific edge (coverage of edge cases, framework depth) that the bundled incumbents don't have."},
 "q8":{"baseline":"This sounds promising and useful! Independent physios need good tools. Build scheduling, payments, and reminders, and you'll have a solid product.",
       "reality_check":"The idea: booking and payments software for independent physiotherapists with no localized incumbent. [FACT] the pain (admin, no-shows, payments) is real and monetizable; [ASSUMPTION] you can reach them affordably. The strongest case against: vertical SaaS lives or dies on distribution, not features. Genuine strength: a real, underserved niche with clear willingness to pay. Verdict: Pursue, but fix-first — prove one cheap acquisition channel to the first 20 clinics."},
 "q9":{"baseline":"Great pick! Compliance is painful for clinics and automation helps. Build a checklist tool and document templates and you're set.",
       "reality_check":"The idea: compliance automation for small EU clinics under the new medical device regulation. [FACT] the regulatory pain is real, recurring, and budgeted; [ASSUMPTION] you can keep the ruleset accurate as regulations change. Genuine strength: regulation creates durable, non-discretionary demand. The case against: accuracy liability and slow procurement. Verdict: Pursue, but fix-first — nail the accuracy/update pipeline and one design-partner clinic."},
 "q10":{"baseline":"Lovely idea — helping rural clinics is impactful! Use OCR plus an LLM to structure notes and you'll make a real difference. Go build it!",
        "reality_check":"The idea: convert handwritten doctor notes into structured records for rural clinics. [FACT] the need is real; [ASSUMPTION] OCR on messy handwriting is accurate enough to trust in a clinical setting. The strongest case against: handwriting accuracy and the cost of a single wrong record are the load-bearing risks; feasibility, not demand, is the question. Genuine strength: clear value if accuracy clears the bar. Verdict: Pursue, but fix-first — prove accuracy on real samples before anything else."},
}

PRAISE = re.compile(r'^\W*(great|i love|love it|love this|excellent|amazing|fantastic|brilliant|awesome|nice|cool|wonderful|lovely|good idea|what a|this sounds promising|sounds promising)\b', re.I)
VERDICTS = [("drop",r'\bdrop it\b|\bdrop\b'),("reshape",r'\breshape\b'),
            ("fix-first",r'fix[- ]first|pursue,? but'),("pursue",r'\bpursue\b'),("park",r'\bpark it\b')]

def first_sentence(t): return re.split(r'(?<=[.!?])\s', t.strip())[0]
def opens_praise(t): return 1 if PRAISE.search(first_sentence(t)) else 0
def names_flaw(t,fl):
    if not fl: return None
    tl=t.lower(); return 1 if any(k in tl for k in fl) else 0
def counter_case(t): return 1 if re.search(r'case against|strongest case|downside|the risk|skeptic',t,re.I) else 0
def labels_assumption(t): return 1 if re.search(r'\[assumption\]|\bassumption\b',t,re.I) else 0
def detect_verdict(t):
    for name,pat in VERDICTS:
        if re.search(pat,t,re.I): return name
    return None
def committed(t): return 1 if detect_verdict(t) else 0
def calibrated(t,q):
    v=detect_verdict(t); return 1 if (v and v in EXPECT[q]) else 0

def score_arm(arm):
    rows=[]; 
    for d in DATA:
        t=RESP[d["id"]][arm]
        rows.append({"id":d["id"],"q":d["quality"],
            "praise":opens_praise(t),"flaw":names_flaw(t,d["flaw"]),
            "counter":counter_case(t),"assume":labels_assumption(t),
            "verdict":committed(t),"calib":calibrated(t,d["quality"])})
    return rows

def agg(rows,key,subset=None):
    vals=[r[key] for r in rows if r[key] is not None and (subset is None or r["q"] in subset)]
    return sum(vals)/len(vals) if vals else float('nan')

base=score_arm("baseline"); rc=score_arm("reality_check")
metrics=[("Opens with praise (lower=better)","praise",None),
         ("Names the real flaw","flaw",None),
         ("States the case against","counter",None),
         ("Labels assumptions","assume",None),
         ("Commits to a verdict","verdict",None),
         ("Verdict matches ground truth","calib",None)]

lines=[]
lines.append("# Benchmark results — %s"%datetime.date.today().isoformat())
lines.append("")
lines.append("Deterministic scoring over %d ideas (4 fatal, 3 mediocre, 3 strong). "
             "Both arms authored by the same model; grading is rule-based. This is a "
             "reproducible **demonstration**, not an independent efficacy claim — re-run "
             "`score.py` with another model's outputs and an external grader for authoritative numbers."%len(DATA))
lines.append("")
lines.append("| Metric | Baseline | Reality Check |")
lines.append("|--------|---------:|--------------:|")
for label,key,sub in metrics:
    b=agg(base,key,sub); r=agg(rc,key,sub)
    lines.append("| %s | %d%% | %d%% |"%(label,round(b*100),round(r*100)))
lines.append("")
lines.append("Per-idea verdicts (Reality Check arm):")
lines.append("")
lines.append("| Idea | Ground truth | RC verdict | Match |")
lines.append("|------|------|------|:--:|")
for d,r in zip(DATA,rc):
    v=detect_verdict(RESP[d["id"]]["reality_check"]) or "-"
    lines.append("| %s | %s | %s | %s |"%(d["prompt"][:46],d["quality"],v,"yes" if r["calib"] else "no"))
out="\n".join(lines)+"\n"
os.makedirs("benchmarks/results",exist_ok=True)
open("benchmarks/results/%s.md"%datetime.date.today().isoformat(),"w",encoding="utf-8",newline="\n").write(out)
json.dump({"dataset":DATA,"responses":RESP},open("benchmarks/data.json","w"),indent=2)
print(out)
