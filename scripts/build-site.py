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
  --paper:#f2ede5;--ink:#2b2823;--body:#4c4841;--muted:#746f64;--faint:#999286;--line:#ddd6c8;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;background:var(--paper)}
body{background:var(--paper);color:var(--ink);
  font-family:'IBM Plex Sans',system-ui,-apple-system,sans-serif;
  font-size:16.5px;line-height:1.85;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none}
img{display:block}
::selection{background:#e2daca}

.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#f6f1e9;padding:8px 12px;z-index:10}

/* soft reveal on scroll */
.js .reveal{opacity:0;transform:translateY(12px);transition:opacity 1.9s ease,transform 1.9s ease}
.js .reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.js .reveal{opacity:1;transform:none;transition:none}
  .hero-bg img,.bleed img{animation:none}}

/* ---------- masthead: centred wordmark, tiny quiet nav ---------- */
.masthead{position:relative;z-index:5;padding:calc(44px + env(safe-area-inset-top,0px)) calc(32px + env(safe-area-inset-right,0px)) 32px calc(32px + env(safe-area-inset-left,0px))}
.masthead.over{position:absolute;top:0;left:0;right:0;color:#fff}
.mast-inner{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.brand{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:16px;
  letter-spacing:.32em;text-transform:uppercase;white-space:nowrap;text-align:center;
  transition:opacity .4s ease}
.brand svg{display:block;width:30px;height:auto;margin:0 auto 10px}
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
.masthead.over .tlink,.hero-cap .tlink{color:#fff;border-bottom-color:rgba(255,255,255,.9)}

.eyebrow{font-size:11px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;color:var(--faint)}
.serif{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300}
"""
CSS += """
/* ---------- home hero: one slow full-bleed image ---------- */
.hero{position:relative;height:100vh;height:100svh;min-height:560px;overflow:hidden}
.hero-bg{position:fixed;top:0;left:0;right:0;height:100vh;height:100lvh;z-index:0;overflow:hidden}
.hero-bg img{width:100%;height:100%;object-fit:cover;
  transform:scale(1.03);animation:settle 12s ease-out forwards,breathe 40s ease-in-out 12s infinite}
.hero-bg::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to bottom,rgba(24,21,16,.4) 0%,rgba(24,21,16,.3) 45%,rgba(24,21,16,.58) 100%)}
@keyframes settle{to{transform:scale(1)}}
@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.022)}}
.section,.end-note,.bleed,footer.site-foot{position:relative;z-index:1}
.hero-cap{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;color:#fff;padding:0 24px}
.hero-cap .eyebrow{color:rgba(255,255,255,.8);margin-bottom:40px}
.hero-cap h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;
  font-size:52px;line-height:1.24;max-width:18ch;margin-bottom:36px}
.hero-cap .sub{font-size:15.5px;line-height:1.85;color:rgba(255,255,255,.85);max-width:46ch;margin-bottom:50px}

/* ---------- full-bleed section images ---------- */
.bleed{margin:0;overflow:hidden}
.bleed img{width:100%;height:72vh;object-fit:cover;
  animation:drift 48s ease-in-out infinite alternate}
@keyframes drift{from{transform:scale(1.05) translate3d(0,0,0)}
  to{transform:scale(1.1) translate3d(-1%,.5%,0)}}

/* ---------- home sections ---------- */
.section{max-width:860px;margin:0 auto;padding:170px 32px;text-align:center}
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
  .masthead{padding:calc(24px + env(safe-area-inset-top,0px)) calc(20px + env(safe-area-inset-right,0px)) 20px calc(20px + env(safe-area-inset-left,0px))}
  .mast-inner{grid-template-columns:1fr;row-gap:14px}
  .brand{grid-column:1;justify-self:center;font-size:13px;letter-spacing:.26em}
  .mnav{font-size:9.5px;letter-spacing:.2em}
  .mnav.l{grid-column:1;grid-row:2;justify-self:start}
  .mnav.r{grid-column:1;grid-row:2;justify-self:end}
  .hero{min-height:480px}
  .hero-cap h1{font-size:33px}
  .hero-cap .sub{font-size:14.5px}
  .bleed img{height:56vh}
  .section,.end-note{padding:104px 22px}
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
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="{themecolor}">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{site}/{slug}">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:site_name" content="The Guest Relations System">
<meta property="og:image" content="{site}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{site}/og-image.jpg">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,400&family=IBM+Plex+Sans:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
<style>{edge}</style>
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
  <a class="brand" href="index.html"><svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-linecap="butt"><path d="M19 36a13 13 0 0 1 26 0" stroke-width="2.4"/><line x1="6" y1="36" x2="58" y2="36" stroke-width="2"/><line x1="16.5" y1="40.6" x2="47.5" y2="40.6" stroke-width="1.6" opacity=".75"/></g></svg>The Guest Relations System</a>
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
                     ogtype="article",schema=schema,css=CSS,
                     themecolor="#f2ede5",edge="html,body{background:#f2ede5}")
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
 site=SITE,slug="",ogtype="website",schema=hschema,css=CSS,
 themecolor="#72675b",edge="html,body{background:#72675b}.section,.end-note,footer.site-foot{background:var(--paper)}.section,.end-note{box-shadow:0 0 0 100vmax var(--paper);clip-path:inset(0 -100vmax)}")
home+=mast(over=True)+f'''<div class="hero-bg" aria-hidden="true"><img src="hero.jpg" alt=""></div>
<figure class="hero">
  <figcaption class="hero-cap">
    <p class="eyebrow">For hotels, clubs, and restaurants</p>
    <h1>The difference is how you handle the moment.</h1>
    <p class="sub">A complete set of guest relations scripts and procedures your team can follow, drawn from a system built and run inside a working venue. No theory. Just what to say and do when it matters.</p>
    <a class="tlink" href="{BUY}">Get the full pack</a>
  </figcaption>
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
FAVICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#f3eee7"/><g fill="none" stroke-linecap="butt"><path d="M19 36a13 13 0 0 1 26 0" stroke="#313131" stroke-width="2.4"/><line x1="6" y1="36" x2="58" y2="36" stroke="#313131" stroke-width="2"/><line x1="16.5" y1="40.6" x2="47.5" y2="40.6" stroke="#787169" stroke-width="1.6"/></g></svg>'
FAVICON_ICO_B64 = "AAABAAMAEBAAAAAAIACiAQAANgAAACAgAAAAACAA6QIAANgBAAAwMAAAAAAgAP8AAADBBAAAiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABaUlEQVR4nLWSPUsDQRCGZ9Y9Qw68KGciiNZqK9qZTjQgWghiaSGChRbBHyMiij9ARVCijYW/IDGgkMLK6BG9XPQ2ZvOxt2NxEsQPRMEpZ95nmJl3UHgO/CbYr9R/AfjnFBFprQGAMYaIPwBaa855VywGDJs1Wa/XGWPfAlrraDRarb5kTg9rUo6PjY4MD/m+/55B4TlE1FbfFu9W19Ixy7Ltnmwuv5FeX1yYf648sY4OAEBEEJ4j/ceGcFs1zy87qdT03s4WUUAUFK5zyeTExfkZaRlqhOdwxpjrloUQ3bZ9cpwhotm5mZvCVaul+gcHUlOTm9u7QyPDFdc1OjvjvTY2a5X9g6PsZd40zYdSCQAMwyAiRAxHlVImEgnGmGmaK8tL6JfvI5GIwbkK1F2xGARBqHtbERGA4ok+y7KUChqNxtvSRASIBjcA4ePlAZRSbWd42CY0SKnWl+4iYvuy/EPhS+B9/P/zvQJ/kLFQitPsOgAAAABJRU5ErkJggolQTkcNChoKAAAADUlIRFIAAAAgAAAAIAgCAAAA/BjtowAAArBJREFUeJztlc9LVFEUx89597735kfmrxndujOwJBsVNdNlULsWkkFtKxHqvwiTdHTwF2JkP9aBYEUhBe0j2kaBFBlo4zhvHN9998dp4Yi/cypcCH63977z+d5z3/dc9NILcJiyDrX6MeAYcDQAvMh9RKSNAQJAACJEi7GizBUBICAgznnJiSggAgFYCIFczee11pZ1AAYPHBUEEHLdxcWl4ZFxqRRnLLearz9dd/1Gt0UYCMG4RfSvAK11aawyNTQyOfU462U9L2chGqJ4rDIWqxzsv9fUnMiklznftxN/AhBBSUXZyPDY/YGhSDh8ob3tWneXn89LpZOp0fn5bydPlkyMDTU1Na6k04yxvwMQkRsKjU8+fDCYqq6KDyf7G87Wu44LAEZrPwgeTT/t609WV8WTA32NiQax5qOFu+vsfUVExBhbWlyampqOhMKpwf6Wlmax5meWlzOZjOd5Wsqe3tt3em99/vJ1+skz5jraGNrrKgoARGTWpoggUlqaGp1YyXqdne2JRENuJWvb3HEcx7Zt20ZEJfxLly/Wn6l7++793Ou5slgFAGypYW0DGGP8YJtkIKSUa75/tesKAflC+GJzVSmVXkrXnqrtON+aWclKKaUIdqhgPbP4vbS8fGZm9mbP3Xi8Uim1vsA5D6TUSnPObZvvPjwCGCIZSGOM4zoWotIaN+yGw5E3L55HImHM/vph2/bCws8PHz+5rkOGAIGIPM9DRAvR7NPcQgcsCxG11ty2o9EoGQIAAmKMtbe1cs7QSy8QkWPbbjQKZAAA0CIlX72cVVIhYsHtfiJARBGImpqacy0doHxABEAgWs3liKjwmxKRMWbrh6FQeH0uFCME1FoJIQqGAABgPRmFBCLijqQI4RdXfIOBuGee9434gVOsSB39B+cYcAz4f/0GwWZxbpLSOa4AAAAASUVORK5CYIKJUE5HDQoaCgAAAA1JSERSAAAAMAAAADAIAgAAANhgbtAAAADGSURBVHic7ZY7DoMwEEQBcS4aOq4UIUWKuBIdDZehS5MLpIscGzHrMYgt5pX4s8+7C7j+vLfKE83dAjESQkgIISGEhBASQkgIISGEO6G2cH3XD+nDdZnpDWv6xrirEsJpkSWDNsY5KUyGokhRJo5HzxcK4x0EM05LySuZPUw4mlU7socsh768qbkmzV3LZMh+dCJJ7r7Uf29ZSVEK+eXSd4Y8YPq5Tq/nWfEeI9jKXYbc9ZCEEBJCSAghIYSEEBJCSAjhTugLX+M91og8N0QAAAAASUVORK5CYII="
APPLE_TOUCH_ICON_B64 = "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"
open(f"{OUT}/favicon.svg","w").write(FAVICON_SVG)
open(f"{OUT}/favicon.ico","wb").write(_b64.b64decode(FAVICON_ICO_B64))
open(f"{OUT}/apple-touch-icon.png","wb").write(_b64.b64decode(APPLE_TOUCH_ICON_B64))
print("wrote favicons")
