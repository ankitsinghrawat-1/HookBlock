# HookBlock 🛡️
### *Real-Time Phishing Detection & Security Guard*

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Platform: Chrome](https://img.shields.io/badge/Platform-Chrome-blue.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**HookBlock** is a specialized browser extension designed to protect users from deceptive "Hook" links. By analyzing URL structures and domain metadata, it flags phishing attempts before they can compromise your data.

---

## 📺 Live Demonstration

| 🚦 Detection Logic | 🛠️ User Interface |
| :--- | :--- |
| ![Security Alert GIF](assets/alert-demo.gif) | ![Settings GIF](assets/ui-demo.gif) |
| *Instantly blocks navigation to high-risk URLs.* | *Clean, minimal popup for security stats.* |

---

## 🚀 Core Features
* **Pattern Recognition:** Detects typosquatting (e.g., `g00gle.com` vs `google.com`).
* **Zero-Latency Scanning:** Background scripts ensure your browsing speed isn't affected.
* **Visual Warnings:** High-visibility alerts that prevent accidental clicks on malicious links.
* **Privacy-Centric:** All detection logic stays on your device. No browsing history is ever uploaded.

## 💻 Technical Implementation
* **Manifest V3:** Built using the latest Chrome Extension standards for better security and performance.
* **JavaScript (ES6):** Core engine for URI parsing and heuristic analysis.
* **Content Scripts:** Injects protection directly into the browsing context without slowing down DOM rendering.

## 📦 How to Install
1. **Clone the Project:**
   ```bash
   git clone [https://github.com/ankitsinghrawat-1/hookblock.git](https://github.com/ankitsinghrawat-1/hookblock.git)
2. **Open Extensions:** Navigate to chrome://extensions/ in Chrome.

3. **Developer Mode:** Toggle the switch in the top-right corner.

4. **Load Unpacked:** Click the button and select the hookblock folder.
