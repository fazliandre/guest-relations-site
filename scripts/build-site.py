import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","site")
os.makedirs(OUT,exist_ok=True)
SITE="https://fazliandre.github.io/guest-relations-site"

# The Gumroad product link. Set this to the real URL once the product is
# listed; every "Get the full pack" button on the site picks it up. While it
# is "#" the buttons are dead, which is the one thing still outstanding.
BUY="#"

CSS = """
:root{color-scheme:only light;
  
  --paper:#fbfaf7;--ink:#191a1c;--muted:#5a5d63;--faint:#8a8d93;
  --accent:#1c3d5a;--accent-2:#0f2537;--line:#e6e2da;--fill:#f2efe9;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;background:#fbfaf7 !important;}
body{background:#fbfaf7 !important;color:#191a1c !important;
  font-family:'IBM Plex Sans',system-ui,-apple-system,sans-serif;
  font-size:19px;line-height:1.72;-webkit-font-smoothing:antialiased;}
a{color:var(--accent)}
.masthead,.wrap,.hero,.articles,.home-cta,.home-foot,footer,section,article,div{background-color:transparent}
.masthead{background:#fbfaf7 !important}
.wrap,.hero,.articles,.home-cta,.home-foot{background:#fbfaf7 !important}
h1,h2,h3,h4,p,li,span{color:inherit}
.cta,.cta *{color:#eef2f6}
.cta h3{color:#fff}
.cta .btn{color:#0f2537}
.takeaway{background:#ffffff !important}

.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 12px;z-index:10;border-radius:3px}

/* header */
.masthead{border-bottom:1px solid var(--line);padding:18px 28px;background:var(--paper);}
.masthead-inner{max-width:820px;margin:0 auto;display:flex;align-items:center;
  justify-content:space-between;gap:20px;}
.brand{font-size:12px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
  color:var(--accent);text-decoration:none;}
.nav{font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;letter-spacing:0.02em}
.nav:hover{color:var(--accent)}

.wrap{max-width:720px;margin:0 auto;padding:60px 28px 96px}
.eyebrow{font-size:12px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
  color:var(--faint);margin-bottom:20px;}
h1{font-family:'IBM Plex Serif',Georgia,serif;font-weight:600;font-size:43px;
  line-height:1.14;letter-spacing:-0.015em;margin-bottom:24px;}
.lede{font-size:22px;line-height:1.5;margin-bottom:14px}
.lede-2{font-size:20px;color:var(--muted)}
.rule{width:52px;height:2px;background:var(--accent);margin:38px 0 0}
h2{font-family:'IBM Plex Serif',serif;font-weight:600;font-size:26px;
  line-height:1.25;margin:52px 0 6px;}
.step-label{font-size:11px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;
  color:var(--accent);display:block;margin-bottom:10px;}
p{margin-bottom:18px;color:#26282b}
.script{background:var(--fill);border-left:3px solid var(--accent);padding:18px 22px;
  margin:22px 0;font-style:italic;color:#33363a;font-size:18px;line-height:1.6;border-radius:2px;}
.script-label{display:block;font-style:normal;font-size:11px;font-weight:600;
  letter-spacing:0.18em;text-transform:uppercase;color:var(--accent);margin-bottom:8px;}
hr{border:none;border-top:1px solid var(--line);margin:62px 0}

/* takeaway box */
.takeaway{border:1px solid var(--line);border-radius:5px;padding:26px 28px;margin:50px 0 0;background:#fff}
.takeaway .eyebrow{margin-bottom:14px}
.takeaway ul{list-style:none;margin:0}
.takeaway li{position:relative;padding-left:22px;margin-bottom:10px;font-size:18px;color:#26282b}
.takeaway li:last-child{margin-bottom:0}
.takeaway li:before{content:"";position:absolute;left:0;top:12px;width:8px;height:2px;background:var(--accent)}

/* cta */
.cta{background:var(--accent);border-radius:6px;padding:38px 36px;color:#eef2f6;}
.cta .eyebrow{color:#9bb4c9;margin-bottom:14px}
.cta h3{font-family:'IBM Plex Serif',serif;font-weight:600;font-size:25px;
  margin-bottom:12px;color:#fff;line-height:1.25;}
.cta p{color:#cdd8e2;font-size:17px;margin-bottom:22px}
.btn{display:inline-block;font-size:13px;font-weight:600;letter-spacing:0.12em;
  text-transform:uppercase;color:var(--accent-2);background:#fff;padding:14px 28px;
  border-radius:4px;text-decoration:none;}
.btn:hover{background:#f0f0ec}
.btn-solid{color:#fff;background:var(--accent)}
.btn-solid:hover{background:var(--accent-2)}

/* related */
.related{margin-top:58px}
.related .eyebrow{margin-bottom:16px}
.related a{display:block;text-decoration:none;color:inherit;border-top:1px solid var(--line);
  padding:18px 0;transition:padding-left .15s ease}
.related a:hover{padding-left:6px}
.related a:last-child{border-bottom:1px solid var(--line)}
.related h4{font-family:'IBM Plex Serif',serif;font-weight:500;font-size:19px;color:var(--ink)}

footer{border-top:1px solid var(--line);margin-top:56px;padding-top:26px;
  color:var(--faint);font-size:14px}
footer a{color:var(--faint)}

/* home */
.hero{max-width:820px;margin:0 auto;padding:84px 28px 38px}
.hero h1{font-size:52px;line-height:1.1;letter-spacing:-0.02em;max-width:16ch}
.hero .sub{font-size:22px;line-height:1.5;color:var(--muted);max-width:56ch;margin-bottom:32px}
.trust{font-size:15px;color:var(--faint);margin-top:20px}
.home-rule{max-width:820px;margin:0 auto}
.articles{max-width:820px;margin:0 auto;padding:60px 28px 36px}
.sec{font-family:'IBM Plex Sans',sans-serif;font-weight:600;font-size:12px;
  letter-spacing:0.2em;text-transform:uppercase;color:var(--faint)}
.list{border-top:1px solid var(--line);margin-top:24px}
a.item{display:block;text-decoration:none;color:inherit;border-bottom:1px solid var(--line);
  padding:26px 0;transition:padding-left .15s ease}
a.item:hover{padding-left:8px}
a.item h3{font-family:'IBM Plex Serif',serif;font-weight:500;font-size:23px;margin-bottom:6px}
a.item p{font-size:17px;color:var(--muted);max-width:60ch;margin-bottom:0}
a.item .go{font-size:12px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;
  color:var(--accent);margin-top:10px;display:inline-block}
.home-cta{max-width:820px;margin:36px auto 0;padding:0 28px}
.home-foot{max-width:820px;margin:0 auto;padding:0 28px 40px}

@media(max-width:600px){
  body{font-size:18px}
  h1{font-size:33px}
  .hero h1{font-size:35px}
  .lede{font-size:20px}
  .hero .sub{font-size:19px}
  .wrap{padding:42px 22px 76px}
  .hero{padding:52px 22px 30px}
  .cta{padding:30px 26px}
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Serif:wght@400;500;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="masthead"><div class="masthead-inner">
  <a class="brand" href="index.html">The Guest Relations System</a>
  <a class="nav" href="index.html">All field notes</a>
</div></div>
'''

ART = '''<article class="wrap" id="main">
  <p class="eyebrow">Field Notes</p>
  <h1>{h1}</h1>
  <p class="lede">{lede1}</p>
  <p class="lede-2">{lede2}</p>
  <div class="rule"></div>
{body}
  <div class="takeaway">
    <p class="eyebrow">In short</p>
    <ul>{takeaway}</ul>
  </div>
  <hr>
  <section class="cta">
    <p class="eyebrow">From the full system</p>
    <h3>{cta_h}</h3>
    <p>{cta_p}</p>
    <a class="btn" href="{BUY}">Get the full pack</a>
  </section>
  <section class="related">
    <p class="eyebrow">Read next</p>
{related}
  </section>
  <footer>The Guest Relations System &middot; Written for hotels, clubs, and restaurants. &middot; <a href="index.html">All field notes</a></footer>
</article>
</body>
</html>'''

def sec(label, head, paras):
    out = f'  <h2><span class="step-label">{label}</span>{head}</h2>\n'
    for p in paras:
        if p.startswith("SCRIPT:"):
            out += f'  <div class="script"><span class="script-label">What to say</span>{p[7:]}</div>\n'
        else:
            out += f'  <p>{p}</p>\n'
    return out

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
 h1="How to Handle a Guest No-Show",
 lede1="A no-show costs you a table, a room, or a booking you could have given to someone else. Handled badly, it also costs you the guest.",
 lede2="Here is a calm, repeatable way to deal with one, so the same situation never catches your team off guard twice.",
 body=b,
 takeaway=["Ask for a reply the day before, not just a reminder.",
           "Agree your hold window in advance so nobody improvises.",
           "Call once, warmly, before you release the space.",
           "Follow up the next day without a hint of blame.",
           "Record it, because the pattern matters more than the night."],
 cta_h="This is one of twelve modules.",
 cta_p="The no-show process above is a single part of the Guest Relations System, a complete set of hospitality scripts and procedures you can drop straight into your venue.",
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
 h1="How to Handle a Difficult Guest",
 lede1="A difficult guest is not a threat. Handled well, they are often your most loyal guest afterwards, because you were the one who stayed calm.",
 lede2="Here is a steady, repeatable way through it, so you never improvise under pressure.",
 body=b,
 takeaway=["Let them finish before you say anything at all.",
           "Repeat the problem back in your own words.",
           "Fix the real issue plainly rather than smothering it in gestures.",
           "Match what you offer to the size of the mistake.",
           "Note the pattern, then let the night go."],
 cta_h="This is one of twelve modules.",
 cta_p="The process above is a single part of the Guest Relations System, a complete set of hospitality scripts and procedures you can drop straight into your venue.",
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
 h1="How to Recover a Guest After Something Goes Wrong",
 lede1="Things go wrong in every venue. What separates the good ones is not that they never slip, it is what they do in the ninety seconds afterwards.",
 lede2="Here is the recovery process, plainly, so anyone on your team can run it.",
 body=b,
 takeaway=["Respond fast. Speed matters more than the size of the gesture.",
           "Own it, fix it, then come back once more to check.",
           "Match what you give to the size of the mistake.",
           "Set the tiers in advance so staff can act without a manager.",
           "Record it, because repeats point at your operation, not the guest."],
 cta_h="This is one of twelve modules.",
 cta_p="The recovery process above is a single part of the Guest Relations System, a complete set of hospitality scripts and procedures you can drop straight into your venue.",
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
 h1="How to Reply to a Bad Google Review",
 lede1="A bad review feels personal. But your reply is not really to the reviewer, it is to every future guest reading it before they decide to book.",
 lede2="Here is how to answer one so it works in your favour.",
 body=b,
 takeaway=["Write for the next reader, not the person who complained.",
           "Thank, acknowledge, and offer to continue privately.",
           "Never argue the details in public, even when you are right.",
           "Report only what is abusive or clearly fake.",
           "Three reviews about the same thing is data, so fix the cause."],
 cta_h="This is one of twelve modules.",
 cta_p="The written response module this is drawn from includes reply templates for every kind of review, good and bad. It is one part of the Guest Relations System.",
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
 h1="How to Remember Your Regulars",
 lede1="The guest who feels known does not compare you on price. Recognition is the cheapest loyalty you will ever build, and most venues leave it on the table.",
 lede2="Here is how to turn being remembered into a system, not a lucky habit.",
 body=b,
 takeaway=["Recognition is a note taken, not a memory trusted.",
           "Record preferences, occasions, and names on the guest profile.",
           "Read the profile shortly before the guest arrives.",
           "Flag birthdays and anniversaries in advance, never on the night.",
           "Recognition buys attachment where discounts only buy visits."],
 cta_h="This is one of twelve modules.",
 cta_p="The recognition module this is drawn from includes the guest record and occasion system in full. It is one part of the Guest Relations System.",
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
    html=HEAD.format(title=d["title"],meta=d["meta"],site=SITE,slug=slug+".html",
                     ogtype="article",schema=schema,css=CSS)
    html+=ART.format(h1=d["h1"],lede1=d["lede1"],lede2=d["lede2"],body=d["body"],
                     takeaway=tk,cta_h=d["cta_h"],cta_p=d["cta_p"],related=rel,BUY=BUY)
    open(f"{OUT}/{slug}.html","w").write(html)
    print("wrote",slug)

# ---- home ----
items="".join(f'''    <a class="item" href="{s}.html">
      <h3>{P[s]["nav"]}</h3>
      <p>{P[s]["meta"]}</p>
      <span class="go">Read &rarr;</span>
    </a>\n''' for s in order)
hschema=json.dumps({"@context":"https://schema.org","@type":"WebSite",
  "name":"The Guest Relations System","url":SITE})
home=HEAD.format(title="The Guest Relations System — Hospitality Scripts and Procedures",
 meta="A complete set of guest relations scripts and procedures for hotels, clubs, and restaurants. Handle no-shows, difficult guests, recovery, reviews, and recognition with a system your team can follow.",
 site=SITE,slug="",ogtype="website",schema=hschema,css=CSS)
home+=f'''<div class="hero" id="main">
  <p class="eyebrow">For hotels, clubs, and restaurants</p>
  <h1>The difference is how you handle the moment.</h1>
  <p class="sub">A complete set of guest relations scripts and procedures your team can follow, drawn from a system built and run inside a working venue. No theory. Just what to say and do when it matters.</p>
  <a class="btn btn-solid" href="{BUY}">Get the full pack</a>
  <p class="trust">Twelve modules &middot; One download &middot; No subscription</p>
</div>
<div style="padding:0 28px"><div class="home-rule"><div class="rule" style="margin:0"></div></div></div>
<section class="articles">
  <p class="sec">Field Notes</p>
  <div class="list">
{items}  </div>
</section>
<div class="home-cta">
  <div class="cta">
    <p class="eyebrow">The complete system</p>
    <h3>Twelve modules. One download.</h3>
    <p>Everything above is a small taste. The full system covers the guest record, recovery, no-shows, difficult guests, recognition, written responses, special occasions, hiring, and more, ready to drop into your venue.</p>
    <a class="btn" href="{BUY}">Get the full pack</a>
  </div>
</div>
<div class="home-foot"><footer>The Guest Relations System &middot; Written for hotels, clubs, and restaurants.</footer></div>
</body></html>'''
open(f"{OUT}/index.html","w").write(home)
print("wrote index")

# sitemap + robots
urls="".join(f"  <url><loc>{SITE}/{s}.html</loc></url>\n" for s in order)
open(f"{OUT}/sitemap.xml","w").write(
 f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{SITE}/</loc></url>\n{urls}</urlset>\n')
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("wrote sitemap, robots")
