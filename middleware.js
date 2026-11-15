// Server-side AI/search crawler visit logger (non-blocking, never rewrites/blocks).
// Posts to CloudPipe spider-track; humans never trigger a request.
const ENDPOINT = 'https://cloudpipe-macao-app.vercel.app/api/v1/spider-track';
const SITE = 'yamanakada';
// Order matters: longer / more specific tokens first (Applebot-Extended before Applebot, etc.)
const BOTS = [
  'Applebot-Extended', 'Google-Extended', 'OAI-SearchBot', 'ChatGPT-User', 'Claude-SearchBot',
  'Perplexity-User', 'meta-externalagent', 'MistralAI-User', 'PerplexityBot', 'DuckAssistBot',
  'Claude-User', 'Claude-Web', 'anthropic-ai', 'ClaudeBot', 'GPTBot', 'Googlebot', 'Bingbot',
  'Applebot', 'Bytespider', 'Amazonbot', 'CCBot', 'YouBot', 'cohere-ai',
];

export const config = {
  runtime: 'edge',
  matcher: [
    '/((?!.*\\.(?:png|jpe?g|gif|webp|avif|svg|ico|css|js|mjs|map|woff2?|ttf|otf|eot|mp4|webm|mp3|pdf|json|webmanifest)$).*)',
  ],
};

export default function middleware(request, context) {
  try {
    const ua = request.headers.get('user-agent') || '';
    if (!ua) return;
    const lower = ua.toLowerCase();
    const bot = BOTS.find((b) => lower.includes(b.toLowerCase()));
    if (!bot) return;
    const url = new URL(request.url);
    const task = fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        site: SITE,
        bot_name: bot,
        path: url.pathname + url.search,
        referer: request.headers.get('referer') || undefined,
        ua: ua.slice(0, 500),
      }),
    }).catch((e) => console.error('spider-track failed:', e && e.message));
    if (context && typeof context.waitUntil === 'function') context.waitUntil(task);
  } catch (e) {
    console.error('spider-track error:', e && e.message);
  }
  return; // undefined = continue, request untouched
}
