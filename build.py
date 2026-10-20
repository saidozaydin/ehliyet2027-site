from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent / 'docs'
ORIGIN = 'https://saidozaydin.github.io'
BASE_PATH = '/ehliyet2027-site'
EMAIL = 'ehliyet2027destek@gmail.com'
DATE = '21 Ekim 2026'
NAV = [('/', 'Ana sayfa'), ('/gizlilik/', 'Gizlilik'), ('/hesap-silme/', 'Hesap silme')]


def page(path, title, description, content):
    navigation = ''.join(f'<a href="{url}"' + (' aria-current="page"' if url == path else '') + f'>{label}</a>' for url, label in NAV)
    return f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — Ehliyet 2027 · SaOz</title>
<meta name="description" content="{escape(description, quote=True)}"><meta name="theme-color" content="#147d59">
<link rel="canonical" href="{ORIGIN}{BASE_PATH}{path}"><link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
</head><body><a class="skip" href="#icerik">İçeriğe geç</a>
<header><a class="brand" href="/" aria-label="Ehliyet 2027 ana sayfa"><span class="mark" aria-hidden="true">↗</span><span>Ehliyet <strong>2027</strong></span></a>
<nav aria-label="Ana menü">{navigation}</nav></header>
<main id="icerik">{content}</main>
<footer><div><a class="brand" href="/">Ehliyet 2027</a><p>Yayıncı: <strong>SaOz</strong><br>Ehliyet Sınav Soruları 2027</p></div>
<div><span class="eyebrow">İletişim</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div class="footer-links"><a href="/gizlilik/">Gizlilik politikası</a><a href="/hesap-silme/">Hesap ve veri silme</a><a href="/kosullar/">Kullanım koşulları</a></div>
<p class="footnote">© 2026 SaOz. Bağımsız bir çalışma uygulamasıdır; MEB veya başka bir resmî kurumun uygulaması değildir.</p></footer>
</body></html>'''


home = '''<section class="hero"><div><p class="eyebrow">SaOz · Android çalışma uygulaması</p>
<h1>Ehliyet sınavına<br><em>kendi hızında</em><br>hazırlan.</h1>
<p class="lead">Sorularla çalış, yanlışlarına dön, trafik işaretlerini öğren. Ehliyet Sınav Soruları 2027, hazırlık sürecini günlük bir alışkanlığa dönüştürmene yardımcı olur.</p>
<div class="status"><span></span>Google Play yayını hazırlanıyor</div></div>
<aside class="study-sheet" aria-label="Uygulamanın çalışma alanları"><span class="eyebrow">Bir sonraki adımın</span><h2>Bugün ne öğrenelim?</h2>
<div class="study-row"><span class="number">01</span><div><h3>Soru ve denemeler</h3><p>Bilgini ölç, açıklamayla öğren.</p></div><span aria-hidden="true">↗</span></div>
<div class="study-row"><span class="number">02</span><div><h3>Trafik işaretleri</h3><p>İşaretleri görerek karşılaştır.</p></div><span aria-hidden="true">↗</span></div>
<div class="study-row"><span class="number">03</span><div><h3>Kısa tekrarlar</h3><p>Bilgi kartlarıyla pekiştir.</p></div><span aria-hidden="true">↗</span></div>
<div class="sheet-note"><span aria-hidden="true">✓</span>Misafir olarak da çalışabilirsin.</div></aside></section>
<section class="features" aria-labelledby="calisma"><p class="eyebrow">Hazırlık, adım adım</p><h2 id="calisma">Sadece çözmekle kalma.<br>Nedenini de öğren.</h2>
<div class="feature-grid"><article><span class="feature-symbol" aria-hidden="true">↗</span><h3>Açıklamalı sorular</h3><p>İlk yardım, trafik, araç tekniği ve trafik adabı konularında çalış. Denemelerde zamanını yönet.</p></article>
<article><span class="feature-symbol" aria-hidden="true">↻</span><h3>Sana ait tekrarlar</h3><p>Yanlışlarını ve favorilerini yeniden ziyaret et. İşaretler, kavşaklar ve bilgi kartlarıyla öğrendiklerini pekiştir.</p></article>
<article><span class="feature-symbol" aria-hidden="true">✓</span><h3>İlerlemen yanında</h3><p>Cihazında misafir olarak çalış. İstersen Google hesabınla giriş yaparak hesabındaki ilerlemeyi cihazların arasında eşitle.</p></article></div></section>
<section class="privacy-callout"><div><p class="eyebrow">Verilerin üzerinde kontrol</p><h2>Nasıl çalıştığını bil.</h2><p>Hangi bilgilerin kullanıldığını, hesabını nasıl silebileceğini ve bize nasıl ulaşacağını açıkça paylaşıyoruz.</p></div>
<div class="resource-links"><a href="/gizlilik/">Gizlilik politikasını oku <span aria-hidden="true">↗</span></a><a href="/hesap-silme/">Hesap ve veri silme <span aria-hidden="true">↗</span></a><a href="mailto:ehliyet2027destek@gmail.com">Destek ekibine yaz <span aria-hidden="true">↗</span></a></div></section>'''

privacy = f'''<article class="document"><p class="eyebrow">SaOz · Ehliyet Sınav Soruları 2027</p><h1>Gizlilik politikası</h1><p class="date">Son güncelleme: {DATE}</p>
<p class="intro">Bu politika, SaOz tarafından sunulan Ehliyet 2027 uygulamasında ve bu tanıtım sitesinde bilgilerin nasıl kullanıldığını açıklar. Destek ve veri talepleri için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine ulaşabilirsiniz.</p>
<h2>1. Misafir kullanımı ve cihazdaki bilgiler</h2><p>Uygulamayı hesap oluşturmadan kullanabilirsiniz. Cevaplar, favoriler, yanlışlar, deneme sonuçları, çalışma ve öğrenme ilerlemesi ile görünüm tercihleri cihazda saklanır. Ana ekran widget'ı kullanılırsa günlük çalışma özeti cihazdaki widget ile paylaşılır.</p>
<h2>2. Google ile giriş ve hesap bilgileri</h2><p>Google ile giriş seçildiğinde Google hesabınıza ait ad, e-posta adresi, sağlayıcı kimliği ve oturum için gereken kimlik doğrulama bilgileri işlenir. İlk girişte uygulama hesabınız oluşturulur. Kimlik doğrulama ve uygulama oturumu Supabase Auth aracılığıyla sağlanır. Google şifreniz uygulamaya verilmez. Uygulama Google Drive, Gmail veya kişilerinize erişim istemez.</p>
<h2>3. Bulut eşitlemesi</h2><p>Giriş yaptığınızda hesabınıza ait çalışma ilerlemesi Supabase üzerinde saklanır ve aynı hesapla giriş yaptığınız cihazlar arasında eşitlenir. Bu ilerleme cevaplar, sınav sonuçları, favoriler, yanlışlar, öğrenme kayıtları ve çalışma tercihlerini içerebilir. Çevrimdışı değişiklikler bağlantı yeniden kurulduğunda gönderilir. Misafir ilerlemesi yalnızca aktarımı seçtiğinizde hesabınıza eklenir.</p>
<h2>4. Amaçlar ve hizmet sağlayıcılar</h2><p>Bilgiler; giriş yapmak, ilerlemeyi saklamak ve eşitlemek, içerik güncellemelerini iletmek, teknik sorunları incelemek ve destek taleplerini yanıtlamak için kullanılır. Mevcut uygulama sürümü reklam gösterimi veya reklam amaçlı profilleme yapmaz.</p><p>Google kimlik sağlayıcısıdır; Supabase kimlik doğrulama, veritabanı ve içerik hizmetleri sunar. Ağ bağlantıları hizmet sağlayıcılarına IP adresi, istek zamanı ve teknik bağlantı bilgileri iletebilir. İçerik güncelleme isteğine cevap geçmişi veya sınav sonuçları eklenmez. Hizmet sağlayıcıların altyapıları farklı ülkelerde bulunabilir. Destek adresine yazarsanız e-posta adresiniz ve mesaj içeriğiniz de talebiniz kapsamında işlenir.</p><p>Bu tanıtım sitesi GitHub Pages üzerinde barındırılır. GitHub, site ziyaretçilerinin IP adreslerini güvenlik amacıyla kaydeder. Sayfalara tarafımızdan reklam veya ziyaretçi analizi kodu eklenmemiştir. Sağlayıcıların kendi veri uygulamaları için <a href="https://policies.google.com/privacy">Google</a>, <a href="https://supabase.com/privacy">Supabase</a> ve <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub</a> gizlilik açıklamalarını inceleyebilirsiniz.</p>
<h2>5. Saklama, sıfırlama ve silme</h2><p>Misafir bilgileri siz sıfırlayana veya cihazdaki uygulama verilerini temizleyene kadar cihazda kalır. Hesap ve bulut ilerlemesi, hesabınız etkin olduğu sürece saklanır. Uygulama içindeki hesap silme işlemi başarıyla tamamlandığında uygulama hesabınız ve buna bağlı etkin bulut ilerlemeniz silinir; o cihazdaki hesap kaydı temizlenir.</p><p>Çıkış yapmak veya uygulamayı kaldırmak bulut hesabını silmez. İlerlemeyi sıfırlamak da hesabı kapatmaz. Misafir kaydı ayrı tutulur. Diğer cihazlardaki çevrimdışı kopyaları kaldırmak için o cihazlarda uygulama verilerinin de temizlenmesi gerekebilir. Hizmet sağlayıcıların teknik kayıt ve yedeklerine ilişkin işlemler kendi hizmet politikalarına tabidir; etkin hesap silme işlemi bu kayıtlardaki tüm kopyaların aynı anda fiziksel olarak silindiği anlamına gelmez.</p><p><a href="/hesap-silme/">Hesap ve veri silme sayfasından</a> uygulama içi adımları görebilir veya e-posta ile silme talebi gönderebilirsiniz. Destek yazışmaları ve teknik kayıtların ayrıntılı saklama süreleri hakkında destek adresinden bilgi isteyebilirsiniz.</p>
<h2>6. Güvenlik ve kontrol</h2><p>Uygulamanın production hizmet bağlantıları HTTPS kullanır. Google oturumu, cihaz kaydı ve hesabınıza ait ilerleme uygulamanın işlevleri için kullanılır. İnternet üzerinden veya cihazlarda veri saklamanın tamamen risksiz olduğu garanti edilemez. Destek talebinde Google şifrenizi, tek kullanımlık kodları veya oturum belirteçlerini göndermeyin.</p>
<h2>7. İletişim ve güncellemeler</h2><p>Bilgilerinize erişim, düzeltme, silme veya uygulamanın veri işleyişiyle ilgili talepler için yayıncı SaOz'a <a href="mailto:{EMAIL}">{EMAIL}</a> adresinden ulaşabilirsiniz. Talebin ilgili hesap sahibinden geldiğini doğrulamak için gerekli bilgiler istenebilir. Uygulamanın veri işleyişi değişirse bu sayfa ve güncelleme tarihi yenilenir.</p></article>'''

subject = quote('Ehliyet 2027 hesabımı ve verilerimi silme talebi')
body = quote('Merhaba SaOz,\nEhliyet 2027 uygulama hesabımın ve hesabımla ilişkili bulut verilerimin silinmesini istiyorum.\nUygulamaya giriş yaptığım e-posta adresi: \n')
deletion = f'''<article class="document"><p class="eyebrow">SaOz · Ehliyet Sınav Soruları 2027</p><h1>Hesap ve<br>veri silme</h1><p class="date">Son güncelleme: {DATE}</p>
<p class="intro">Ehliyet 2027 hesabınızı ve bu hesaba bağlı çalışma verilerini silmek için uygulamayı kullanabilir veya SaOz'a e-posta ile talep gönderebilirsiniz.</p>
<h2>Uygulama içinden silme</h2><ol class="steps"><li>Google hesabınızla uygulamaya giriş yapın.</li><li><strong>Profil → Ayarlar → Hesabım → Hesabımı sil</strong> yolunu açın.</li><li>Silme uyarısını inceleyin ve işlemi onaylayın. İnternet bağlantısı gerekir.</li></ol>
<p>İşlem başarıyla tamamlandığında uygulama hesabınız ve hesabınıza bağlı etkin bulut ilerlemeniz silinir. Hesap silme geri alınamaz. İşlem başarısız olursa uygulama hata gösterir; tekrar deneyebilirsiniz.</p>
<h2>Uygulamaya erişemiyorsanız</h2><p>Uygulamayı yeniden yüklemeden de <a href="mailto:{EMAIL}">{EMAIL}</a> adresine <strong>“Ehliyet 2027 hesabımı ve verilerimi silme talebi”</strong> konusuyla yazabilirsiniz. Talebi, mümkünse uygulamada giriş yaptığınız e-posta adresinden gönderin ve uygulama hesabınızın ve ona bağlı bulut verilerinin silinmesini istediğinizi belirtin.</p>
<a class="button" href="mailto:{EMAIL}?subject={subject}&amp;body={body}">Silme talebi e-postasını hazırla <span aria-hidden="true">↗</span></a><p class="small">Bu düğme e-posta uygulamanızda bir taslak açar. Talebin gönderilmesi için e-postayı kendiniz göndermelisiniz. E-posta uygulamanız yoksa yukarıdaki adresi kopyalayabilirsiniz.</p>
<p>SaOz, talebin ilgili hesap sahibinden geldiğini doğrulamak için sizinle iletişim kurabilir. Kimlik doğrulandıktan sonra uygulama hesabı ve ilişkili etkin bulut kayıtları silinir, sonuç e-posta ile bildirilir. Google şifrenizi, tek kullanımlık kodları veya oturum belirteçlerini göndermeyin.</p>
<h2>Hangi veriler silinir?</h2><p>Uygulamanın Supabase hesabı, hesapla ilişkili profil ve kimlik doğrulama kaydı ile cevaplar, deneme sonuçları, favoriler, yanlışlar ve öğrenme ilerlemesi dahil etkin bulut çalışma kaydı silinir. Bu işlem Google hesabınızı veya Google'ın diğer hizmetlerindeki bilgilerinizi silmez.</p>
<h2>Cihazdaki kopyalar</h2><p>Misafir ilerlemesi hesap verilerinden ayrı tutulur. Misafir verilerini <strong>İlerlemeyi sıfırla</strong> seçeneğiyle veya cihaz ayarlarından uygulama verilerini temizleyerek kaldırabilirsiniz. Diğer cihazlarda kalan çevrimdışı kopyaları o cihazlarda da temizlemeniz gerekebilir. Yalnızca uygulamayı kaldırmak buluttaki hesabınızı silmez.</p>
<p>Hizmet sağlayıcıların teknik kayıt ve yedeklerinin işlenmesi kendi politikalarına tabidir. Ayrıntılar için <a href="/gizlilik/">gizlilik politikasını</a> inceleyebilir veya destek adresine yazabilirsiniz.</p></article>'''

terms = f'''<article class="document"><p class="eyebrow">SaOz · Ehliyet Sınav Soruları 2027</p><h1>Kullanım koşulları</h1><p class="date">Son güncelleme: {DATE}</p>
<p class="intro">Ehliyet 2027, SaOz tarafından sunulan bağımsız bir ehliyet sınavına hazırlık ve çalışma uygulamasıdır.</p>
<h2>Çalışma amacı</h2><p>Sorular, açıklamalar, bilgi kartları, işaretler ve senaryolar öğrenmeye yardımcı olmak için sunulur. Uygulama MEB veya başka bir resmî kurumun uygulaması değildir ve resmî sınav hizmeti sunmaz. Kullanım, sınav başarısı veya sürücü belgesi kazanma garantisi vermez. Güncel resmî duyurular ve eğitmeninizin yönlendirmeleri esas alınmalıdır.</p>
<h2>Hesap ve ilerleme</h2><p>Misafir kullanım mümkündür. Google ile giriş seçilirse ilk girişte uygulama hesabı oluşturulur. Hesap güvenliği için Google hesabınıza erişimi koruyun. İlerleme ve eşitlemenin nasıl çalıştığı <a href="/gizlilik/">gizlilik politikasında</a>, hesap silme adımları <a href="/hesap-silme/">hesap silme sayfasında</a> açıklanır.</p>
<h2>Güvenli kullanım</h2><p>Uygulamayı araç kullanırken kullanmayın. Çizimler, senaryolar ve direksiyon hazırlık listeleri uygulamalı sürücü eğitimini veya gerçek yol koşullarına göre karar vermeyi ikame etmez.</p>
<h2>İçerik ve teknik geri bildirim</h2><p>Bir içerik hatası veya teknik sorun fark ederseniz ilgili ekranı ve sorunu <a href="mailto:{EMAIL}">{EMAIL}</a> adresine bildirebilirsiniz. Şifre veya kimlik doğrulama kodu göndermeyin. Uygulama ve içerikler güncellenebilir; çevrimdışı kopyalar güncelleme alınana kadar eski bilgileri içerebilir.</p></article>'''

pages = [('/', 'Ana sayfa', 'SaOz Ehliyet 2027: açıklamalı sorular, denemeler, trafik işaretleri ve bilgi kartlarıyla ehliyet sınavına hazırlan.', home),
         ('/gizlilik/', 'Gizlilik politikası', 'Ehliyet 2027 ve SaOz: Google ile giriş, çalışma verileri, bulut eşitlemesi ve gizlilik bilgileri.', privacy),
         ('/hesap-silme/', 'Hesap ve veri silme', 'Ehliyet 2027 uygulama hesabınızı ve ilişkili verilerinizi silmek için uygulama ve e-posta adımları.', deletion),
         ('/kosullar/', 'Kullanım koşulları', 'SaOz Ehliyet 2027 uygulamasının çalışma amacı ve kullanım bilgileri.', terms)]
for path, title, description, content in pages:
    target = ROOT / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page(path, title, description, content).replace('href="/', f'href="{BASE_PATH}/'), encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}{BASE_PATH}/sitemap.xml\n', encoding='utf-8')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{ORIGIN}{BASE_PATH}{path}</loc></url>' for path, *_ in pages) + '</urlset>', encoding='utf-8')
print('Built 4 public information pages.')
