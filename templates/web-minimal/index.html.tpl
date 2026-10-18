<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>%%APP_NAME_HTML%%</title>
  <style>
    :root { font-family: system-ui, -apple-system, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif; color: #273b39; background: #f6f7f2; }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100dvh; display: grid; place-items: center; padding: 24px; }
    main { width: min(100%, 520px); border: 1px solid #d6ddd5; border-radius: 24px; background: #fff; padding: clamp(22px, 6vw, 42px); box-shadow: 0 12px 40px #23362c0b; }
    .mark { width: 42px; height: 42px; display: grid; place-items: center; border: 1px solid #acc7b6; border-radius: 12px; font-size: 20px; }
    h1 { margin: 20px 0 12px; font-size: clamp(1.5rem, 5vw, 2rem); line-height: 1.45; letter-spacing: .02em; overflow-wrap: anywhere; }
    p { line-height: 1.8; margin: 0 0 24px; overflow-wrap: anywhere; }
    button { border: 0; border-radius: 12px; padding: 12px 20px; font: inherit; font-weight: 700; background: #266a52; color: white; cursor: pointer; transition: transform .18s ease, background .18s ease; }
    button:hover { background: #1b4e3d; transform: translateY(-2px); }
    button:focus-visible { outline: 3px solid #9eccad; outline-offset: 3px; }
    #status { margin-top: 18px; margin-bottom: 0; font-size: .9rem; color: #456356; }
    @media (prefers-reduced-motion: reduce) { button { transition: none; } button:hover { transform: none; } }
  </style>
</head>
<body>
  <main>
    <div class="mark" aria-hidden="true">✳</div>
    <h1>%%APP_NAME_HTML%%</h1>
    <p>%%DESCRIPTION_HTML%%</p>
    <button id="test" type="button">動作を確認</button>
    <p id="status" role="status" aria-live="polite">小さな試作品の出発点です。</p>
  </main>
  <script>
    document.querySelector("#test").addEventListener("click", () => {
      document.querySelector("#status").textContent = "ボタンの動作を確認しました。";
    });
  </script>
</body>
</html>
