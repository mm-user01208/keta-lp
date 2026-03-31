import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ============================================================
# DESIGN: Add override CSS before </head>
# ============================================================
override_css = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<style>
/* v4 Design Override - minimal modernization */
body { font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, 'Hiragino Kaku Gothic ProN', sans-serif !important; -webkit-font-smoothing: antialiased; }
.top-overview .inner p, .content_text, .faq-text.answer div, .top-block p, .list-payment li { line-height: 1.9; letter-spacing: 0.02em; }
h2 { letter-spacing: 0.04em; }
.top-apply-flow-list-item { border-radius: 10px; }
.top-apply-flow-list-item h3 .top-apply-flow-list-item-header { border-radius: 10px 10px 0 0; }
.faq-item { border-radius: 8px; overflow: hidden; transition: box-shadow 0.2s; }
.faq-item:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.article-list-item { border-radius: 10px; overflow: hidden; transition: box-shadow 0.2s; }
.article-list-item:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
.top-region-list-wrap > div { border-radius: 8px; }
.btn-apply { border-radius: 8px; transition: transform 0.15s, box-shadow 0.15s; }
.btn-apply:hover { transform: translateY(-1px); }
.top-contents .inner section { margin-bottom: 48px; }
.glo-faq-about .faq-list { gap: 6px; }
footer .common-nav section { border-radius: 0; }
footer .common-nav section p { padding: 14px 16px; }
</style>
"""
html = html.replace('</head>', override_css + '</head>')

# ============================================================
# TEXT CHANGES for KW quality improvement
# ============================================================

# Change 1: h2 - add 電子渡航認証 keyword density
old1 = '2021年9月より韓国への入国に<br class="sp-only">電子渡航認証K-ETAが必要となりました。'
new1 = '2021年9月より韓国への入国に<br class="sp-only">電子渡航認証(K-ETA)のオンライン申請が必要となりました。'
if old1 in html:
    html = html.replace(old1, new1)
    changes.append(('h2見出し', old1.replace('<br class="sp-only">', ''), new1.replace('<br class="sp-only">', '')))

# Change 2: top-overview first sentence - add 電子入国申請 / オンライン
old2 = 'K-ETAはビザ(査証)を取得せずに、短期観光・商用を目的として韓国へ入国する渡航者を対象とした電子渡航認証です。'
new2 = 'K-ETA(Korea Electronic Travel Authorization)はビザ(査証)を取得せずに、短期観光・商用を目的として韓国へ入国する渡航者を対象とした電子渡航認証です。オンラインでの申請手続きにより、韓国入国に必要な電子認証を取得できます。'
if old2 in html:
    html = html.replace(old2, new2, 1)
    changes.append(('top-overview冒頭', old2, new2))

# Change 3: STEP1 description - add オンライン申請
old3 = '免責事項と利用規約に同意し、<a href="/form/entry">K-ETA申請書</a>に必要事項を入力してください。K-ETAは年齢を問わず取得が必要です。'
new3 = '免責事項と利用規約に同意し、<a href="/form/entry">K-ETAオンライン申請書</a>に必要事項を入力してください。K-ETAは年齢を問わず取得が必要です。'
if old3 in html:
    html = html.replace(old3, new3)
    changes.append(('STEP1説明文', 'K-ETA申請書', 'K-ETAオンライン申請書'))

# Change 4: K-ETAとは section - add 電子入国カード
old4 = '正式名称は"Korea Electronic Travel Authorization"で、"ケーイーティーエー"や"ケーイータ"と呼ばれます。'
new4 = '正式名称は"Korea Electronic Travel Authorization"(韓国電子入国認証)で、"ケーイーティーエー"や"ケーイータ"と呼ばれます。電子入国カード(e-Arrival Card)とは異なり、K-ETAは入国前にオンラインで申請する電子渡航認証です。'
if old4 in html:
    html = html.replace(old4, new4, 1)
    changes.append(('K-ETAとはセクション', old4, new4))

# Change 5: 注意点 section - add オンライン / 電子申請
old5 = '電子渡航認証K-ETAはビザと比べ手続きが簡易でパスコンやスマートフォン、タブレットを使用して申請が可能です。'
new5 = '電子渡航認証K-ETAはビザと比べ手続きが簡易で、パソコンやスマートフォン、タブレットを使用してオンラインで電子申請が可能です。'
if old5 in html:
    html = html.replace(old5, new5)
    changes.append(('注意点セクション冒頭', old5, new5))

# Change 6: FAQ answer 3 - add オンライン申請
old6 = 'K-ETAはパソコンやスマートフォン、タブレットからオンラインにて申請可能です。'
new6 = 'K-ETAはパソコンやスマートフォン、タブレットからオンラインにて電子申請が可能です。韓国入国に必要な電子渡航認証をオンラインで取得できます。'
if old6 in html:
    html = html.replace(old6, new6, 1)
    changes.append(('FAQ「どのように申請」回答', old6, new6))

# Change 7: 空港セクション h2 - add 電子渡航認証
old7 = '<h2 class="mt-50">K-ETA申請が必要な主要空港</h2>'
new7 = '<h2 class="mt-50">K-ETA(電子渡航認証)申請が必要な主要空港</h2>'
if old7 in html:
    html = html.replace(old7, new7)
    changes.append(('空港セクションh2', 'K-ETA申請が必要な主要空港', 'K-ETA(電子渡航認証)申請が必要な主要空港'))

# Change 8: Payment section - add 韓国入国 オンライン申請
old8 = 'K-ETA申請料金のお支払いはVISA、Mastercard、JCB、Diners Club、American Expressのクレジットカードが利用可能です。'
new8 = '韓国入国に必要なK-ETAオンライン申請料金のお支払いはVISA、Mastercard、JCB、Diners Club、American Expressのクレジットカードが利用可能です。'
if old8 in html:
    html = html.replace(old8, new8)
    changes.append(('お支払い方法', old8, new8))

# ============================================================
# FOOTER: Open first section by default
# ============================================================
# The footer sections use JS toggle. Add a class/style to make first one open.
# Find the first footer common-nav section and add "open" state
old_footer = '<div  id="floating-off"  class="common-nav">\n<section>\n<p><a href="/page_cat/basic-information/">K-ETA基本情報</a><i class="icon icon-plus"></i></p>\n<div class="list-wrap">'
new_footer = '<div  id="floating-off"  class="common-nav">\n<section class="is-open">\n<p><a href="/page_cat/basic-information/">K-ETA基本情報</a><i class="icon icon-minus"></i></p>\n<div class="list-wrap" style="display:block">'
if old_footer in html:
    html = html.replace(old_footer, new_footer)

# Also add JS at the bottom to handle the is-open class
footer_js = """
<script>
// Footer: first section open by default
document.addEventListener('DOMContentLoaded', function(){
  var footerSec = document.querySelector('#floating-off .is-open .list-wrap');
  if(footerSec) footerSec.style.display = 'block';
});
</script>
"""
html = html.replace('</body>', footer_js + '</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Print changes
print("=" * 60)
print("テキスト変更一覧")
print("=" * 60)
for i, (loc, old, new) in enumerate(changes, 1):
    print(f"\n【変更{i}】{loc}")
    print(f"  変更前: {old[:80]}{'...' if len(old)>80 else ''}")
    print(f"  変更後: {new[:80]}{'...' if len(new)>80 else ''}")

print(f"\n合計 {len(changes)} 箇所のテキスト変更")
