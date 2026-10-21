import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","site")
os.makedirs(OUT,exist_ok=True)
SITE="https://theguestrelationssystem.com"

# The Gumroad product link. Set this to the real URL once the product is
# listed; every "Get the full pack" button on the site picks it up. While it
# is "#" the buttons are dead, which is the one thing still outstanding.
BUY="#"

CSS = """
:root{color-scheme:only light;
  --paper:#f8f6f2;--ink:#2b2823;--body:#4c4841;--muted:#7a766d;--faint:#a09a8f;--line:#e3ded4;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;background:var(--paper)}
body{background:var(--paper);color:var(--ink);
  font-family:'IBM Plex Sans',system-ui,-apple-system,sans-serif;
  font-size:16.5px;line-height:1.85;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none}
img{display:block}
::selection{background:#e8e2d5}

.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 12px;z-index:10}

/* soft reveal on scroll */
.js .reveal{opacity:0;transform:translateY(18px);transition:opacity 1.1s ease,transform 1.1s ease}
.js .reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.js .reveal{opacity:1;transform:none;transition:none}}

/* ---------- masthead: centred wordmark, tiny quiet nav ---------- */
.masthead{position:relative;z-index:5;padding:32px}
.masthead.over{position:absolute;top:0;left:0;right:0;color:#fff}
.mast-inner{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.brand{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:16px;
  letter-spacing:.32em;text-transform:uppercase;white-space:nowrap;text-align:center;
  transition:opacity .4s ease}
.brand:hover{opacity:.6}
.mnav{font-size:11px;font-weight:500;letter-spacing:.22em;text-transform:uppercase;
  color:inherit;opacity:.75;transition:opacity .4s ease}
.mnav:hover{opacity:1}
.mnav.l{justify-self:start}.mnav.r{justify-self:end}

/* tiny uppercase links used throughout */
.tlink{display:inline-block;font-size:11.5px;font-weight:500;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ink);padding-bottom:5px;
  border-bottom:1px solid var(--ink);transition:opacity .4s ease}
.tlink:hover{opacity:.55}
.masthead.over .tlink{color:#fff;border-bottom-color:#fff}

.eyebrow{font-size:11px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;color:var(--faint)}
.serif{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300}
"""
CSS += """
/* ---------- home hero: one slow full-bleed image ---------- */
.hero{position:relative;height:100vh;height:100svh;min-height:560px;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  transform:scale(1.04);animation:settle 9s ease-out forwards}
@keyframes settle{to{transform:scale(1)}}
.hero::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to bottom,rgba(24,21,16,.34) 0%,rgba(24,21,16,.18) 42%,rgba(24,21,16,.5) 100%)}
.hero-cap{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;color:#fff;padding:0 24px}
.hero-cap .eyebrow{color:rgba(255,255,255,.82);margin-bottom:30px}
.hero-cap h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;
  font-size:60px;line-height:1.16;max-width:16ch;margin-bottom:26px}
.hero-cap .sub{font-size:16.5px;line-height:1.75;color:rgba(255,255,255,.85);max-width:52ch;margin-bottom:38px}
.hero-cap .trust{margin-top:34px;font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;color:rgba(255,255,255,.62)}
.scroll-cue{position:absolute;left:50%;bottom:34px;transform:translateX(-50%);z-index:2;
  font-size:10px;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.75);text-align:center}
.scroll-cue::after{content:"";display:block;width:1px;height:44px;margin:12px auto 0;
  background:linear-gradient(to bottom,rgba(255,255,255,.75),rgba(255,255,255,0))}

/* ---------- full-bleed section images ---------- */
.bleed{margin:0}
.bleed img{width:100%;height:72vh;object-fit:cover}

/* ---------- home sections ---------- */
.section{max-width:860px;margin:0 auto;padding:150px 32px;text-align:center}
.section .eyebrow{margin-bottom:34px}
.section h2.big{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;
  font-size:46px;line-height:1.18;margin-bottom:26px}
.section .lead{font-size:17px;color:var(--muted);max-width:56ch;margin:0 auto 42px}
.notes-list{margin-top:30px}
.note{padding:74px 0}
.note+.note{border-top:1px solid var(--line)}
.note h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:31px;
  line-height:1.25;margin-bottom:14px;transition:opacity .4s ease}
.note p{font-size:15.5px;color:var(--muted);max-width:54ch;margin:0 auto 22px}
.note a{display:block}
.note a:hover h3{opacity:.6}
.note .tlink{margin-top:2px}
.end-note{padding:150px 32px;text-align:center;max-width:860px;margin:0 auto}
.end-note .eyebrow{margin-bottom:34px}
.end-note h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;
  font-size:44px;line-height:1.18;margin-bottom:24px}
.end-note p{font-size:16.5px;color:var(--muted);max-width:56ch;margin:0 auto 40px}

footer.site-foot{text-align:center;padding:110px 32px 90px;color:var(--faint);
  font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;line-height:2.4}
footer.site-foot a{border-bottom:1px solid var(--faint);padding-bottom:3px;transition:opacity .4s ease}
footer.site-foot a:hover{opacity:.55}
"""
CSS += """
/* ---------- article ---------- */
.a-head{max-width:820px;margin:0 auto;padding:130px 32px 90px;text-align:center}
.a-head .eyebrow{margin-bottom:32px}
.a-head h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;
  font-size:52px;line-height:1.16;margin-bottom:28px}
.a-head .lede{font-size:17.5px;line-height:1.75;color:var(--muted);max-width:54ch;margin:0 auto}
.a-body{max-width:640px;margin:0 auto;padding:96px 28px 40px}
.a-body h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;
  font-size:31px;line-height:1.25;margin:104px 0 24px}
.a-body h2 .step-label{display:block;font-family:'IBM Plex Sans',sans-serif;font-weight:500;
  font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--faint);margin-bottom:16px}
.a-body p{margin-bottom:24px;color:var(--body)}
.say{margin:56px 0}
.say .say-label{display:block;font-family:'IBM Plex Sans',sans-serif;font-weight:500;
  font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--faint);margin-bottom:20px}
.say p{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-weight:400;
  font-size:23px;line-height:1.55;color:var(--ink);margin:0}
.takeaway{margin:110px 0 0}
.takeaway .eyebrow{margin-bottom:30px}
.takeaway ul{list-style:none}
.takeaway li{position:relative;padding-left:26px;margin-bottom:14px;font-size:15.5px;color:var(--body)}
.takeaway li:before{content:"";position:absolute;left:0;top:14px;width:10px;height:1px;background:var(--faint)}
.a-cta{text-align:center;margin:130px 0 0}
.a-cta .eyebrow{margin-bottom:30px}
.a-cta h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:36px;
  line-height:1.2;margin-bottom:18px}
.a-cta p{font-size:16px;color:var(--muted);max-width:52ch;margin:0 auto 34px}
.a-rel{text-align:center;margin:120px 0 0}
.a-rel .eyebrow{margin-bottom:34px}
.a-rel a{display:block;padding:26px 0;transition:opacity .4s ease}
.a-rel a:hover{opacity:.55}
.a-rel a+.a-rel a{border-top:1px solid var(--line)}
.a-rel h4{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:23px;line-height:1.3}
.a-foot{max-width:640px;margin:110px auto 0;padding:0 28px 80px;text-align:center;
  color:var(--faint);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;line-height:2.4}
.a-foot a{border-bottom:1px solid var(--faint);padding-bottom:3px;transition:opacity .4s ease}
.a-foot a:hover{opacity:.55}

/* ---------- phone ---------- */
@media(max-width:640px){
  body{font-size:16px}
  .masthead{padding:24px 20px 20px}
  .mast-inner{grid-template-columns:1fr;row-gap:14px}
  .brand{grid-column:1;justify-self:center;font-size:13px;letter-spacing:.26em}
  .mnav{font-size:9.5px;letter-spacing:.2em}
  .mnav.l{grid-column:1;grid-row:2;justify-self:start}
  .mnav.r{grid-column:1;grid-row:2;justify-self:end}
  .hero{min-height:480px}
  .hero-cap h1{font-size:37px}
  .hero-cap .sub{font-size:15px}
  .bleed img{height:56vh}
  .section,.end-note{padding:92px 22px}
  .section h2.big{font-size:33px}
  .end-note h2{font-size:32px}
  .note{padding:56px 0}
  .note h3{font-size:26px}
  .a-head{padding:88px 22px 60px}
  .a-head h1{font-size:36px}
  .a-body{padding:64px 22px 20px}
  .a-body h2{font-size:26px;margin:76px 0 20px}
  .say p{font-size:20px}
  .a-cta h3{font-size:29px}
  footer.site-foot{padding:76px 22px 64px}
}
"""

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{site}/{slug}">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:site_name" content="The Guest Relations System">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,400&family=IBM+Plex+Sans:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
<script type="application/ld+json">{schema}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<script>document.documentElement.className+=' js';
addEventListener('DOMContentLoaded',function(){{
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{
    if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});
  document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el)}})}});</script>
'''

def mast(over=False):
    cls="masthead over" if over else "masthead"
    return f'''<div class="{cls}"><div class="mast-inner">
  <a class="mnav l" href="index.html#notes">Field notes</a>
  <a class="brand" href="index.html">The Guest Relations System</a>
  <a class="mnav r" href="{BUY}">Get the pack</a>
</div></div>
'''

ART = '''<header class="a-head" id="main">
  <p class="eyebrow">Field notes</p>
  <h1>{h1}</h1>
  <p class="lede">{lede1} {lede2}</p>
</header>
<figure class="bleed"><img src="{img}" alt="{alt}"></figure>
<article class="a-body">
{body}
  <div class="takeaway reveal">
    <p class="eyebrow">In short</p>
    <ul>{takeaway}</ul>
  </div>
  <section class="a-cta reveal">
    <p class="eyebrow">From the full system</p>
    <h3>{cta_h}</h3>
    <p>{cta_p}</p>
    <a class="tlink" href="{BUY}">Get the full pack</a>
  </section>
  <section class="a-rel reveal">
    <p class="eyebrow">Read next</p>
{related}
  </section>
</article>
<footer class="a-foot">The Guest Relations System &middot; Written for hotels, clubs, and restaurants<br><a href="index.html">All field notes</a></footer>
</body>
</html>'''

def sec(label, head, paras):
    out = f'  <h2 class="reveal"><span class="step-label">{label}</span>{head}</h2>\n'
    for p in paras:
        if p.startswith("SCRIPT:"):
            out += f'  <div class="say reveal"><span class="say-label">What to say</span><p>{p[7:]}</p></div>\n'
        else:
            out += f'  <p>{p}</p>\n'
    return out

# Calm, empty photography. One slow image per section, no people.
ART_IMG = {
 "no-show-guests":     ("art-no-show.jpg","An empty table for two by a tall window in a quiet dining room"),
 "difficult-guest":    ("art-difficult.jpg","A quiet, empty hotel bar counter at dusk"),
 "service-recovery":   ("art-recovery.jpg","A ceramic teapot and cup on a stone tray in soft morning light"),
 "reply-to-bad-review":("art-review.jpg","A writing desk with paper and pen beside a window"),
 "guest-recognition":  ("art-recognition.jpg","Folded linen and a small vase on a bed in a serene hotel room"),
}

P = {}

# ---- no-show ----
b  = sec("Before they arrive","Confirm, do not just remind",[
 "Most no-shows are not rudeness. They are forgotten bookings, double plans, or a guest who assumed a cancellation went through when it did not. You prevent more of them with confirmation than with any penalty.",
 "Send one message the day before that asks for a reply, not one that only informs. A reminder is easy to ignore. A question is not.",
 "SCRIPT:Hello [Name], we are looking forward to seeing you tomorrow at [time] for [party size]. Could you reply to confirm you are still coming, so we can hold everything ready for you?",
 "A guest who is no longer coming will often tell you now, while you can still fill the space. That single reply is worth more than any fee."])
b += sec("On the day","Hold the window, then release it",[
 "Decide in advance how long you hold a booking past its start time. Fifteen minutes is common for a table, longer for a room. The point is that the number is agreed before the moment arrives, so no one is improvising while other guests wait.",
 "During that window, try to reach them once, warmly. Something has usually gone wrong on their side, and a call often turns a no-show back into a late arrival.",
 "SCRIPT:Hello [Name], we have your table ready and wanted to check you are on your way. No rush at all, we just want to make sure it is here for you.",
 "If the window passes with no answer, release the space. You have done the considerate thing, and holding it longer only punishes the guests who did turn up."])
b += sec("Afterwards","Follow up without blame",[
 "How you handle the day after decides whether this guest ever comes back. Resist the urge to make them feel bad. Most people already know they missed something, and a warm door is far more valuable than being right.",
 "SCRIPT:Hello [Name], we missed you [today / yesterday] and hope everything is well. Whenever you would like to come in, we would be glad to have you. Just let us know and we will take care of the rest.",
 "This costs you nothing and quietly does two things: it recovers a guest who felt awkward, and it makes clear that you noticed, without ever scolding them."])
b += sec("Every time","Keep the record",[
 "Note it on the guest's profile: the no-show, the reason if you learned one, and whether you reached them. One missed booking is nothing. A pattern tells you whether to take a deposit next time, and whether it was ever really about this guest at all.",
 "A no-show your team handles this way is not a loss. It is a chance to look organised, considerate, and hard to leave."])
P["no-show-guests"]=dict(
 title="How to Handle a Guest No-Show (A Calm, Repeatable Process)",
 meta="A step by step way to handle guest no-shows without losing money or goodwill: the pre-arrival confirmation, the hold window, the follow-up message, and the record you keep.",
 h1="How to handle a guest no-show",
 lede1="A no-show costs you a table, a room, or a booking you could have given to someone else. Handled badly, it also costs you the guest.",
 lede2="Here is a calm, repeatable way to deal with one, so the same situation never catches your team off guard twice.",
 body=b,
 takeaway=["Ask for a reply the day before, not just a reminder.",
           "Agree your hold window in advance so nobody improvises.",
           "Call once, warmly, before you release the space.",
           "Follow up the next day without a hint of blame.",
           "Record it, because the pattern matters more than the night."],
 cta_h="This is one of 39 templates.",
 cta_p="The no-show process above is drawn from the Guest Relations System, the full library of 39 ready to edit guest messages you can drop straight into your venue.",
 nav="How to handle a guest no-show")

# ---- difficult ----
b  = sec("First","Let them finish",[
 "The instinct is to explain, to correct, to defend the team. Do not. An upset guest who gets interrupted only gets more upset, because now they feel unheard on top of whatever went wrong.",
 "Let them say the whole thing. Stay quiet, keep your face open, and do not reach for a solution yet. Most of the heat leaves the moment a person realises they are actually being listened to."])
b += sec("Then","Name it back to them",[
 "Before you fix anything, show them you heard it. Repeat the problem in your own words. This one habit defuses more situations than any discount ever will.",
 "SCRIPT:So the table was booked for seven, you have been waiting twenty minutes, and no one told you why. I understand completely, and I am sorry. Let me sort this out for you now.",
 "You have not admitted fault or given anything away. You have simply proven you were paying attention, which is often all the guest actually wanted."])
b += sec("Now","Fix the thing, not the feeling",[
 "Once they are calm, solve the real problem plainly. Do not over-apologise and do not pile on gestures out of panic. A clear, quick fix reads as competence. A flustered heap of free items reads as guilt.",
 "If you do offer something, make it fit the mistake. A slow drink is a fresh drink, not a free meal. Matching the gesture to the wrong keeps you generous without being taken advantage of."])
b += sec("Never","Take it home",[
 "Some guests are simply having a bad day and you are the nearest target. Handle it with grace, note it if it becomes a pattern, and then let it go. Your team watches how you carry these moments, and calm is contagious."])
P["difficult-guest"]=dict(
 title="How to Handle a Difficult Guest (Without Losing the Room)",
 meta="A calm, repeatable way to handle an upset or difficult guest: let them finish, name the problem back, fix the thing rather than the feeling, and keep your team steady.",
 h1="How to handle a difficult guest",
 lede1="A difficult guest is not a threat. Handled well, they are often your most loyal guest afterwards, because you were the one who stayed calm.",
 lede2="Here is a steady, repeatable way through it, so you never improvise under pressure.",
 body=b,
 takeaway=["Let them finish before you say anything at all.",
           "Repeat the problem back in your own words.",
           "Fix the real issue plainly rather than smothering it in gestures.",
           "Match what you offer to the size of the mistake.",
           "Note the pattern, then let the night go."],
 cta_h="This is one of 39 templates.",
 cta_p="The process above is drawn from the Guest Relations System, the full library of 39 ready to edit guest messages you can drop straight into your venue.",
 nav="How to handle a difficult guest")

# ---- recovery ----
b  = sec("The rule","Speed beats size",[
 "When something goes wrong, how fast you respond matters far more than how much you give. A guest whose problem is solved in two minutes remembers a good night. A guest who waits twenty for a free dessert remembers the wait.",
 "Move first, decide the gesture second. The apology and the fix should reach them before they have to ask twice."])
b += sec("The shape","Own it, fix it, follow up",[
 "Every recovery has the same three beats. Own the problem without excuses. Fix it plainly. Then check back once more so the last thing they feel is care, not the mistake.",
 "SCRIPT:I am so sorry about that, it is on us. I am bringing you a fresh one right now, and I will come back in a moment to make sure it is right.",
 "The follow-up is the part most venues skip, and it is the part guests remember. It turns a fumble into a story about how well you looked after them."])
b += sec("The line","Generous, not guilty",[
 "Match the gesture to the size of the wrong. A small slip earns a sincere apology and a quick fix. A ruined occasion earns something real. Giving away too much for a minor issue trains guests to complain and unsettles your team.",
 "Decide these tiers in advance, so your staff know what they are allowed to offer without finding a manager. Confidence in the moment is worth more than any single free item."])
b += sec("After","Write it down",[
 "Note what went wrong and how you handled it on the guest's record. A one-off is nothing. A repeat is a signal, either about a guest to watch or, more often, about something in your own operation quietly costing you goodwill."])
P["service-recovery"]=dict(
 title="Service Recovery: How to Fix a Bad Guest Experience",
 meta="A simple service recovery process for hospitality: own it, fix it, follow up, and match the gesture to the mistake without giving away the venue.",
 h1="How to recover a guest after something goes wrong",
 lede1="Things go wrong in every venue. What separates the good ones is not that they never slip, it is what they do in the ninety seconds afterwards.",
 lede2="Here is the recovery process, plainly, so anyone on your team can run it.",
 body=b,
 takeaway=["Respond fast. Speed matters more than the size of the gesture.",
           "Own it, fix it, then come back once more to check.",
           "Match what you give to the size of the mistake.",
           "Set the tiers in advance so staff can act without a manager.",
           "Record it, because repeats point at your operation, not the guest."],
 cta_h="This is one of 39 templates.",
 cta_p="The recovery process above is drawn from the Guest Relations System, the full library of 39 ready to edit guest messages you can drop straight into your venue.",
 nav="How to recover a guest after something goes wrong")

# ---- review ----
b  = sec("First","Reply for the next reader, not the reviewer",[
 "You are almost never going to change the mind of the person who left one star. That is not who your reply is for. It is for the hundred future guests reading it, deciding whether to book. Write for them.",
 "A calm, gracious reply to an angry review does more for your reputation than the review did to harm it."])
b += sec("The shape","Thank, acknowledge, take it offline",[
 "A good reply is short and has three parts. Thank them for the feedback, acknowledge the specific thing without arguing, and offer to continue privately. Never relitigate the night in public.",
 "SCRIPT:Thank you for taking the time to share this. I am sorry the evening fell short of what you expected, and I would genuinely like to understand what happened. Please reach out to me directly at [email] so I can make it right.",
 "Notice what this does not do. It does not blame, it does not make excuses, and it does not get into the details. It stays warm and moves the argument off the public page."])
b += sec("Never","Match their heat",[
 "The single biggest mistake is defending yourself. Even when the review is unfair, even when they are simply wrong, a defensive reply makes you look worse than the complaint ever could. Future readers side with the calm party.",
 "If a review is abusive or clearly fake, you can report it. But most poor reviews are just a disappointed person, and a graceful reply is your best answer."])
b += sec("Then","Fix the pattern",[
 "One bad review is noise. Three about the same thing is data. Read them as free consulting on where your operation is quietly failing, and fix the cause rather than only replying to the symptom."])
P["reply-to-bad-review"]=dict(
 title="How to Reply to a Bad Google Review (Restaurants and Venues)",
 meta="How to respond to a negative Google review the right way: write for future readers, thank and acknowledge without arguing, and take the conversation offline.",
 h1="How to reply to a bad Google review",
 lede1="A bad review feels personal. But your reply is not really to the reviewer, it is to every future guest reading it before they decide to book.",
 lede2="Here is how to answer one so it works in your favour.",
 body=b,
 takeaway=["Write for the next reader, not the person who complained.",
           "Thank, acknowledge, and offer to continue privately.",
           "Never argue the details in public, even when you are right.",
           "Report only what is abusive or clearly fake.",
           "Three reviews about the same thing is data, so fix the cause."],
 cta_h="This is one of 39 templates.",
 cta_p="The full library includes reply templates for every kind of review, good and bad. They are part of the 39 ready to edit guest messages in the Guest Relations System.",
 nav="How to reply to a bad Google review")

# ---- recognition ----
b  = sec("Why","Being remembered is the whole product",[
 "Guests can get a good drink almost anywhere. What they cannot get anywhere is the feeling of walking in and being known. That feeling is the most valuable thing your venue sells, and it is almost free to give.",
 "Recognition is not about grand gestures. It is a system for remembering small things and using them at the right moment."])
b += sec("How","Write down the small things",[
 "The magic is not memory, it is a note. When a regular mentions a birthday, a favourite table, a drink they love, the name of a partner, record it on their profile. Then your team can appear to remember effortlessly.",
 "SCRIPT:Welcome back, Mr Tan. Your usual table by the window is ready, and shall I start you with the Negroni?",
 "To the guest this feels like being cared for. To you it is simply a note read thirty seconds before they arrived."])
b += sec("When","Catch the occasions",[
 "Birthdays, anniversaries, first visits, and returns after a long gap are all moments to mark. They cost little and they are exactly what guests tell their friends about afterwards.",
 "Flag them in advance so nothing depends on someone happening to remember in the moment. A quiet card, a small gesture, a line of acknowledgement, timed right, buys years of loyalty."])
b += sec("The point","Loyalty is built, not bought",[
 "Discount schemes buy visits. Recognition buys attachment. A guest who feels known does not shop around on price, because no one else knows them the way you do. That is the cheapest and strongest hold a venue can have."])
P["guest-recognition"]=dict(
 title="Guest Recognition: How to Remember Regulars and Special Occasions",
 meta="A simple system for guest recognition in hospitality: record the small things, greet regulars by name and preference, and catch birthdays and anniversaries.",
 h1="How to remember your regulars",
 lede1="The guest who feels known does not compare you on price. Recognition is the cheapest loyalty you will ever build, and most venues leave it on the table.",
 lede2="Here is how to turn being remembered into a system, not a lucky habit.",
 body=b,
 takeaway=["Recognition is a note taken, not a memory trusted.",
           "Record preferences, occasions, and names on the guest profile.",
           "Read the profile shortly before the guest arrives.",
           "Flag birthdays and anniversaries in advance, never on the night.",
           "Recognition buys attachment where discounts only buy visits."],
 cta_h="This is one of 39 templates.",
 cta_p="The full library includes the recognition and occasion messages in full. They are part of the 39 ready to edit guest messages in the Guest Relations System.",
 nav="How to remember your regulars")

import json
order=list(P.keys())
for slug,d in P.items():
    others=[s for s in order if s!=slug][:3]
    rel="".join(f'    <a href="{s}.html"><h4>{P[s]["nav"]}</h4></a>\n' for s in others)
    tk="".join(f"<li>{t}</li>" for t in d["takeaway"])
    schema=json.dumps({
      "@context":"https://schema.org","@type":"HowTo","name":d["h1"],
      "description":d["meta"],
      "publisher":{"@type":"Organization","name":"The Guest Relations System"}
    })
    img,alt=ART_IMG[slug]
    html=HEAD.format(title=d["title"],meta=d["meta"],site=SITE,slug=slug+".html",
                     ogtype="article",schema=schema,css=CSS)
    html+=mast()+ART.format(h1=d["h1"],lede1=d["lede1"],lede2=d["lede2"],body=d["body"],
                     takeaway=tk,cta_h=d["cta_h"],cta_p=d["cta_p"],related=rel,BUY=BUY,
                     img=img,alt=alt)
    open(f"{OUT}/{slug}.html","w").write(html)
    print("wrote",slug)

# ---- home ----
notes="".join(f'''    <div class="note reveal">
      <a href="{s}.html">
        <h3>{P[s]["nav"]}</h3>
        <p>{P[s]["meta"]}</p>
        <span class="tlink">Read more</span>
      </a>
    </div>\n''' for s in order)
hschema=json.dumps({"@context":"https://schema.org","@type":"WebSite",
  "name":"The Guest Relations System","url":SITE})
home=HEAD.format(title="The Guest Relations System — Hospitality Scripts and Procedures",
 meta="A complete set of guest relations scripts and procedures for hotels, clubs, and restaurants. Handle no-shows, difficult guests, recovery, reviews, and recognition with a system your team can follow.",
 site=SITE,slug="",ogtype="website",schema=hschema,css=CSS)
home+=mast(over=True)+f'''<figure class="hero">
  <img src="hero.jpg" alt="A calm, empty hotel lounge with soft morning light">
  <figcaption class="hero-cap">
    <p class="eyebrow">For hotels, clubs, and restaurants</p>
    <h1>The difference is how you handle the moment.</h1>
    <p class="sub">A complete set of guest relations scripts and procedures your team can follow, drawn from a system built and run inside a working venue. No theory. Just what to say and do when it matters.</p>
    <a class="tlink" href="{BUY}">Get the full pack</a>
    <p class="trust">39 templates &middot; One download &middot; No subscription</p>
  </figcaption>
  <div class="scroll-cue">Scroll</div>
</figure>
<section class="section" id="notes">
  <p class="eyebrow">Field notes</p>
  <h2 class="big">Quiet systems for loud moments.</h2>
  <p class="lead">Short field notes from the floor, each one a calm, repeatable way through a situation every venue meets.</p>
  <div class="notes-list">
{notes}  </div>
</section>
<figure class="bleed reveal"><img src="home-mid.jpg" alt="A still reflecting pool in a quiet resort courtyard at dawn"></figure>
<section class="end-note" id="system">
  <p class="eyebrow">The complete system</p>
  <h2>39 templates. One download.</h2>
  <p>Everything above is a small taste. The full library covers bookings and no-shows, recovery, review replies, recognition and special occasions, VIP and concierge outreach, and the difficult messages: 39 ready to edit templates to drop straight into your venue.</p>
  <a class="tlink" href="{BUY}">Get the full pack</a>
</section>
<figure class="bleed reveal"><img src="home-cta.jpg" alt="A misty stone garden path at dawn"></figure>
<footer class="site-foot">The Guest Relations System<br>Written for hotels, clubs, and restaurants</footer>
</body></html>'''
open(f"{OUT}/index.html","w").write(home)
print("wrote index")

# sitemap + robots
urls="".join(f"  <url><loc>{SITE}/{s}.html</loc></url>\n" for s in order)
open(f"{OUT}/sitemap.xml","w").write(
 f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{SITE}/</loc></url>\n{urls}</urlset>\n')
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

# GitHub Pages reads site/CNAME to serve the custom domain. Derived from SITE
# so the two can never disagree; editing SITE alone is enough.
open(f"{OUT}/CNAME","w").write(SITE.split("://",1)[1].rstrip("/")+"\n")
print("wrote sitemap, robots")
# Favicons: a quiet serif monogram on cream. Generated inside the build so
# the deploy runner needs no extra tools; the ICO and PNG bytes are embedded.
import base64 as _b64
FAVICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#fbfaf7"/><text x="32" y="43" font-family="Georgia, \'Times New Roman\', serif" font-size="38" fill="#191a1c" text-anchor="middle">G</text></svg>'
FAVICON_ICO_B64 = "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"
APPLE_TOUCH_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAIAAACyr5FlAAAU5klEQVR4nO2deZRVxZnAv6q669u76YW9gYbQgCIoAVokuCAKJlFnjjMxmjlJNDlOJjlZjOS4EOOg0SQuxDiT0Rg0Go0xSIyCEKNmNMkYh0WMGhlotgYa6IXu12+5a1XNH0U3HeSG169fw31N/f5oHq/fu/f2rd+t76u6VXWR51ogkRwPfKoPQBJepBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJApBySQKQckkCkHJJAlFN9AKcMzjnnXLzofefYDyGE+rwU/+vz3hDndJGD9wEhTAhWFAVhBaBfJc04o5RSxphQCyFACCM0NI0Z4nJwzhljAKAoClH03vep73R1pTs6Ojq7ujo7O9PpdDaby+fzvu/7vs85EIJVVTUMI2Ka8UQimYgnk8lUKpVKJWOxmKZH+uyEUd/zfV9ohzEaMqIMTTmEEwghTTdEXmVbuaamnX/94IMPPti6bdv2vXv3tra1pdPdlmW5ritqAsZ4b2zpCSAIIYQxwpgYhm6aZiIeH1Y1bMTw4XV1YydMGD+xvn7c+LoRw0foRrRn377Y4BFNylkUNMSetyKKWdd1QAoA7Nmz6803//ynP725afPm5ua96XQ3pT4hRFEURVEVhfQtQvGjz8aOJiHCNsYYpdT3fd+nlFKEQNO0VCo5auSoyZM/MmPG9JkzzpoypWFYVa34FvUd3/cBQOzlZJ6HkjB05GCMAXBNjwLAoYMtr7z62m9eWLNx46bW1lYOYOi6pmmKoiCEepMPOG4SGgzqW58g4Bw4577vu67nei6j1DDMESNqp02beu65jfPObTxj2jQzEgMAzjzXdaHcLBkKchypLYwoAGzZsvmpp59Zs2bt3r37MMaRSERVVTiSkLICTfhw+f0dh1AfGGOu69q27ft+NBqtr59wbmPjxRdfNHfOnIrKYQDAqOt5HkII4zLoRCh7OXyfGqYJgDds2PDjH//XS+vWZzKZaDSm6xr0eHPC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"
open(f"{OUT}/favicon.svg","w").write(FAVICON_SVG)
open(f"{OUT}/favicon.ico","wb").write(_b64.b64decode(FAVICON_ICO_B64))
open(f"{OUT}/apple-touch-icon.png","wb").write(_b64.b64decode(APPLE_TOUCH_ICON_B64))
print("wrote favicons")
