KITO Website V11 — Multilingual SEO

Six independently crawlable static pages: /vi/, /en/, /zh/, /ja/, /fr/, /ru/.
Each includes server-readable language-specific title, description, Open Graph and Twitter tags.
The selector navigates to the corresponding URL. Policy modal URLs remain /LANG/?policy=privacy or sales.

IMPORTANT BEFORE GO-LIVE:
1. Upload this entire kito-site directory as the website root on your HTTPS domain.
2. Run: python configure-domain.py https://YOUR-REAL-DOMAIN
   Run this BEFORE upload, or on the deployed source before publishing.
3. This fills in absolute canonical, hreflang, og:image and twitter:image URLs.
   Placeholder __SITE_ORIGIN__ is intentionally not a real URL; it cannot generate a working social preview until configured.
4. Test Facebook Sharing Debugger and other social preview tools after deployment; cache may require refresh.
5. Check all six URLs and policy links. Root / redirects to /en/.
6. Do not set a fictitious domain in SEO tags.

Image: assets/seo/kito-og-1200x630.jpg (exact 1200x630).
