#!/usr/bin/env python3
"""src/page.html（給 Claude Artifact 用的片段）→ index.html（GitHub Pages 用的完整文件）。
改內容只改 src/page.html，然後 `python3 build.py`。"""
import pathlib

HERE = pathlib.Path(__file__).parent
frag = (HERE / "src" / "page.html").read_text(encoding="utf-8")

TITLE = "AI 革命真正的戰場"
DESC = "2026/10 奇美醫院教學部師培中心 CFD 課程・聽眾帶走版。五個樂章、柏拉圖的洞穴，與各職類下週能做的一件事。"

HEAD = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<!-- 院內講義，給拿到連結的學員看；不希望被搜尋引擎收錄 -->
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="article">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#127963;</text></svg>">
<style>img,svg,video{{max-width:100%;height:auto}}</style>
</head>
<body>
"""

(HERE / "index.html").write_text(HEAD + frag + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html written")
