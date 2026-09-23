import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Hero Video
hero_target = """            <div class="max-w-lg sm:max-w-3xl mx-auto rounded-2xl sm:rounded-3xl overflow-hidden border border-white/10 bg-slate-900 shadow-2xl shadow-teal-500/20">
                <div class="video-frame">
                    <iframe src="https://drive.google.com/file/d/1eSdBHXiiw68QkHaWHj4vFYphiUZKuw3n/preview" allow="autoplay; encrypted-media" allowfullscreen loading="lazy" title="فيديو تعريفي عن خدماتنا"></iframe>
                </div>
            </div>"""
hero_new = """            <div class="max-w-lg sm:max-w-3xl mx-auto rounded-2xl sm:rounded-3xl overflow-hidden border border-white/10 bg-slate-900 shadow-2xl shadow-teal-500/20">
                <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/wkppticcrg.js" async type="module"></script><style>wistia-player[media-id='wkppticcrg']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/wkppticcrg/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="wkppticcrg" aspect="1.7777777777777777"></wistia-player>
            </div>"""
content = content.replace(hero_target, hero_new)

# Locate the portfolio grid
start_str = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
end_str = '            </div>\n        </div>\n    </section>\n\n    <!-- Differentiation Section: Us vs Traditional Agencies -->'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_grid = """<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Video 1 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/77eucu1brw.js" async type="module"></script><style>wistia-player[media-id='77eucu1brw']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/77eucu1brw/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="77eucu1brw" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. محمود عيد – أخصائي أطفال وحديثي الولادة، جامعة القاهرة</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">+50 مليون مشاهدة و+250 ألف متابع أورجانيك بدون إعلانات ممولة</p>
                    </div>
                </div>
                <!-- Video 2 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/vggdr404b4.js" async type="module"></script><style>wistia-player[media-id='vggdr404b4']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/vggdr404b4/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="vggdr404b4" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. بلال العزبي – مدرس جراحة الأطفال بجامعة القاهرة</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">بدأ صفحات السوشيال ميديا معانا من الصفر، واستمر التعاون لأكتر من سنتين، وحققنا خلالها انتشار ونجاح قوي.</p>
                    </div>
                </div>
                <!-- Video 3 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/mxhfq1o6ri.js" async type="module"></script><style>wistia-player[media-id='mxhfq1o6ri']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/mxhfq1o6ri/swatch'); display: block; filter: blur(5px); padding-top:177.78%; }</style> <wistia-player media-id="mxhfq1o6ri" aspect="0.5625"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. عبدالرحمن السبع – رئيس قسم جراحة الأطفال بمستشفى المنيرة</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">بعد تجارب متعددة مع شركات ميديا، بدأنا التعاون من أجل بناء حضور رقمي أكثر تأثيرًا، وحققنا نتائج ملموسة في زيادة حجوزات الكشوفات والعمليات.</p>
                    </div>
                </div>
                <!-- Video 4 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/lu7a58ifod.js" async type="module"></script><style>wistia-player[media-id='lu7a58ifod']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/lu7a58ifod/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="lu7a58ifod" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. محمد رجب – مدرس أمراض الذكورة بجامعة القاهرة</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">بدأ معانا من سنة، وبنينا السوشيال ميديا والموقع الإلكتروني من الصفر، وحققنا ظهورًا متقدمًا للموقع في نتائج بحث جوجل.</p>
                    </div>
                </div>
                <!-- Video 5 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/evoxxn8ngr.js" async type="module"></script><style>wistia-player[media-id='evoxxn8ngr']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/evoxxn8ngr/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="evoxxn8ngr" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. أحمد عيد – مدير مركز Kids Care الطبي</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">مركز طبي متكامل يضم وحدة عناية مركزة وحضانات، ومستمرين في التعاون من أكتر من سنة، قدرنا خلالها نحقق نتائج قوية وملموسة في الحضور والانتشار على السوشيال ميديا.</p>
                    </div>
                </div>
                <!-- Video 6 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/llj9fnhocb.js" async type="module"></script><style>wistia-player[media-id='llj9fnhocb']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/llj9fnhocb/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="llj9fnhocb" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. محمد خضر – استشاري أول جراحة الأنف والأذن والحنجرة</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">حققنا معاه نتائج قوية على جوجل والسوشيال ميديا، وانعكس ده بشكل واضح على حجوزات العيادة والعمليات.</p>
                    </div>
                </div>
                <!-- Video 7 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/ebz22iuu4e.js" async type="module"></script><style>wistia-player[media-id='ebz22iuu4e']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/ebz22iuu4e/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="ebz22iuu4e" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">المؤسسة المصرية لأطباء الأطفال في مصر</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">حققنا ملايين المشاهدات وآلاف المتابعين بشكل أورجانيك، بدون الاعتماد على إعلانات ممولة على السوشيال ميديا.</p>
                    </div>
                </div>
                <!-- Video 8 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/pudztpmao5.js" async type="module"></script><style>wistia-player[media-id='pudztpmao5']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/pudztpmao5/swatch'); display: block; filter: blur(5px); padding-top:177.78%; }</style> <wistia-player media-id="pudztpmao5" aspect="0.5625"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. محمد هلال – أستاذ النساء والتوليد بجامعة الأزهر</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">مستمرين في التعاون معاه من أكتر من سنة، وحققنا انتشارًا قويًا على السوشيال ميديا انعكس بشكل واضح على حجوزات العيادة والعمليات.</p>
                    </div>
                </div>
                <!-- Video 9 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/wnaohs863e.js" async type="module"></script><style>wistia-player[media-id='wnaohs863e']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/wnaohs863e/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="wnaohs863e" aspect="1.7777777777777777"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">د. علاء سليمان – أخصائي جراحة العيون</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">مستمرين في التعاون معاه من أكتر من 3 سنين، وحققنا خلالها انتشارًا قويًا وحضورًا احترافيًا على السوشيال ميديا.</p>
                    </div>
                </div>
                <!-- Video 10 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/r5mag2kl55.js" async type="module"></script><style>wistia-player[media-id='r5mag2kl55']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/r5mag2kl55/swatch'); display: block; filter: blur(5px); padding-top:177.78%; }</style> <wistia-player media-id="r5mag2kl55" aspect="0.5625"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-0">تعاون مع منصة خليجية لتقديم محتوى تعليمي متخصص للجمهور في الخليج.</h3>
                    </div>
                </div>
                <!-- Video 11 -->
                <div class="glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-teal-500/50 transition-all reveal">
                    <script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/beamxqw2rj.js" async type="module"></script><style>wistia-player[media-id='beamxqw2rj']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/beamxqw2rj/swatch'); display: block; filter: blur(5px); padding-top:177.78%; }</style> <wistia-player media-id="beamxqw2rj" aspect="0.5625"></wistia-player>
                    <div class="p-4 sm:p-5">
                        <h3 class="text-base font-bold text-white mb-2">دكتور مصطفى، أخصائي تقويم الأسنان</h3>
                        <p class="text-sm text-teal-300 leading-relaxed mb-0">في بداية ظهوره على السوشيال ميديا، بدأنا نشتغل على بناء حضوره الرقمي وتقديم محتوى طبي احترافي يعكس خبرته بشكل بسيط وواضح.</p>
                    </div>
                </div>
"""

content = content[:start_idx] + new_grid + content[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
