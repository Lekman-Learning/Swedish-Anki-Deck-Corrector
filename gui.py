"""
Anki-Svenska GUI — Modern PySide6 app
Kontrollera och uppdatera Anki-kort mot Svenska.se med lokal AI.
"""

import json
import re
import sys
import time
from pathlib import Path

from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QFont, QColor, QShortcut, QKeySequence, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QSpinBox, QProgressBar,
    QTextEdit, QStackedWidget, QTableWidget, QTableWidgetItem,
    QHeaderView, QFrame, QSlider, QSplitter, QLineEdit,
    QMessageBox, QCheckBox,
)

from bs4 import BeautifulSoup

import anki_connect
import svenska_scraper as scraper_mod
import synonymer_scraper
import comparator
import updater


# ─────────────────────────────────────────────────────────────
# THEME
# ─────────────────────────────────────────────────────────────

COLORS = {
    "bg":         "#0d1117",
    "surface":    "#161b22",
    "card":       "#21262d",
    "border":     "#30363d",
    "text":       "#e6edf3",
    "subtext":    "#7d8590",
    "accent":     "#3498db",
    "accent_h":   "#58a6ff",
    "green":      "#2ea043",
    "green_bg":   "#12261e",
    "red":        "#f85149",
    "red_bg":     "#2d1214",
    "yellow":     "#d29922",
    "yellow_bg":  "#2a2115",
    "blue_bg":    "#121d2f",
}

STYLESHEET = f"""
QMainWindow {{
    background: {COLORS['bg']};
}}
QWidget {{
    color: {COLORS['text']};
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}}
QLabel {{
    background: transparent;
}}

/* ── Buttons ── */
QPushButton {{
    background: {COLORS['card']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: 500;
    color: {COLORS['text']};
}}
QPushButton:hover {{
    background: {COLORS['border']};
    border-color: {COLORS['accent']};
}}
QPushButton:pressed {{
    background: {COLORS['accent']};
}}
QPushButton:disabled {{
    color: {COLORS['subtext']};
    border-color: {COLORS['card']};
}}

/* ── Accent button ── */
QPushButton#accent {{
    background: {COLORS['accent']};
    border: none;
    color: white;
    font-weight: 600;
}}
QPushButton#accent:hover {{
    background: {COLORS['accent_h']};
}}
QPushButton#accent:disabled {{
    background: {COLORS['border']};
    color: {COLORS['subtext']};
}}

/* ── Danger button ── */
QPushButton#danger {{
    background: {COLORS['red_bg']};
    border: 1px solid {COLORS['red']};
    color: {COLORS['red']};
}}
QPushButton#danger:hover {{
    background: {COLORS['red']};
    color: white;
}}

/* ── Sidebar nav ── */
QPushButton#nav {{
    background: transparent;
    border: none;
    border-radius: 10px;
    padding: 12px;
    text-align: left;
    font-size: 14px;
}}
QPushButton#nav:hover {{
    background: {COLORS['card']};
}}
QPushButton#nav:checked {{
    background: {COLORS['blue_bg']};
    color: {COLORS['accent']};
    font-weight: 600;
}}

/* ── Combo/Spin ── */
QComboBox, QSpinBox {{
    background: {COLORS['card']};
    border: 1px solid {COLORS['border']};
    border-radius: 6px;
    padding: 6px 10px;
    min-height: 28px;
}}
QComboBox:hover, QSpinBox:hover {{
    border-color: {COLORS['accent']};
}}
QComboBox::drop-down {{
    border: none;
    width: 24px;
}}
QComboBox QAbstractItemView {{
    background: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    selection-background-color: {COLORS['accent']};
}}

/* ── Progress bar ── */
QProgressBar {{
    background: {COLORS['card']};
    border: none;
    border-radius: 6px;
    height: 12px;
    text-align: center;
    font-size: 10px;
    color: {COLORS['subtext']};
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {COLORS['accent']}, stop:1 #a855f7);
    border-radius: 6px;
}}

/* ── Text areas ── */
QTextEdit {{
    background: {COLORS['card']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    padding: 8px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
}}

/* ── Tables ── */
QTableWidget {{
    background: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    gridline-color: {COLORS['border']};
}}
QTableWidget::item {{
    padding: 6px;
}}
QTableWidget::item:selected {{
    background: {COLORS['blue_bg']};
    color: {COLORS['accent']};
}}
QHeaderView::section {{
    background: {COLORS['card']};
    border: none;
    border-bottom: 2px solid {COLORS['border']};
    padding: 8px;
    font-weight: 600;
    color: {COLORS['subtext']};
}}

/* ── Slider ── */
QSlider::groove:horizontal {{
    background: {COLORS['card']};
    height: 6px;
    border-radius: 3px;
}}
QSlider::handle:horizontal {{
    background: {COLORS['accent']};
    width: 18px;
    height: 18px;
    margin: -6px 0;
    border-radius: 9px;
}}
QSlider::sub-page:horizontal {{
    background: {COLORS['accent']};
    border-radius: 3px;
}}

/* ── Scroll ── */
QScrollArea {{
    border: none;
    background: transparent;
}}
QScrollBar:vertical {{
    background: {COLORS['bg']};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background: {COLORS['border']};
    border-radius: 4px;
    min-height: 30px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

/* ── Checkbox ── */
QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 2px solid {COLORS['border']};
    background: {COLORS['card']};
}}
QCheckBox::indicator:checked {{
    background: {COLORS['accent']};
    border-color: {COLORS['accent']};
}}
"""


# ─────────────────────────────────────────────────────────────
# HELPER WIDGETS
# ─────────────────────────────────────────────────────────────

def make_card(parent=None) -> QFrame:
    f = QFrame(parent)
    f.setStyleSheet(f"""
        QFrame {{
            background: {COLORS['surface']};
            border: 1px solid {COLORS['border']};
            border-radius: 12px;
        }}
    """)
    return f


def stat_badge(label: str, value: str, color: str, bg: str) -> tuple:
    """Returns (frame, value_label) so caller has a direct reference."""
    frame = QFrame()
    frame.setFixedHeight(90)
    frame.setMinimumWidth(140)
    frame.setStyleSheet(f"""
        QFrame {{
            background: {bg};
            border: 1px solid {color};
            border-radius: 12px;
            padding: 12px;
        }}
    """)
    lay = QVBoxLayout(frame)
    lay.setContentsMargins(14, 10, 14, 10)

    val = QLabel(value)
    val.setFont(QFont("Segoe UI", 26, QFont.Bold))
    val.setStyleSheet(f"color: {color}; background: transparent;")
    lay.addWidget(val)

    lbl = QLabel(label)
    lbl.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 11px; background: transparent;")
    lay.addWidget(lbl)

    return frame, val


def heading(text: str, size: int = 20) -> QLabel:
    lbl = QLabel(text)
    lbl.setFont(QFont("Segoe UI", size, QFont.Bold))
    lbl.setStyleSheet("background: transparent;")
    return lbl


def subtext(text: str) -> QLabel:
    lbl = QLabel(text)
    lbl.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 12px; background: transparent;")
    return lbl


def format_eta(start_time: float, current: int, total: int) -> str:
    """Beräkna och formatera ETA."""
    if current <= 0:
        return ""
    elapsed = time.time() - start_time
    per_item = elapsed / current
    remaining = per_item * (total - current)
    if remaining < 60:
        return f"~{int(remaining)}s kvar"
    return f"~{int(remaining // 60)}m {int(remaining % 60)}s kvar"


def h_line() -> QFrame:
    line = QFrame()
    line.setFixedHeight(1)
    line.setStyleSheet(f"background: {COLORS['border']};")
    return line


# ─────────────────────────────────────────────────────────────
# CARD PREVIEW WIDGET
# ─────────────────────────────────────────────────────────────

class CardPreview(QFrame):
    """Visar ett Anki-kort med framsida/baksida."""

    def __init__(self, title="Kort", parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            CardPreview {{
                background: {COLORS['surface']};
                border: 1px solid {COLORS['border']};
                border-radius: 12px;
            }}
        """)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 12, 16, 12)

        self._title = QLabel(title)
        self._title.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self._title.setStyleSheet(f"color: {COLORS['subtext']}; background: transparent;")
        lay.addWidget(self._title)

        self._word = QLabel()
        self._word.setFont(QFont("Georgia", 28, QFont.Bold))
        self._word.setStyleSheet(f"color: {COLORS['text']}; background: transparent;")
        self._word.setWordWrap(True)
        lay.addWidget(self._word)

        lay.addWidget(h_line())

        self._body = QLabel()
        self._body.setTextFormat(Qt.RichText)
        self._body.setWordWrap(True)
        self._body.setStyleSheet(f"color: {COLORS['text']}; font-size: 14px; background: transparent; line-height: 1.5;")
        lay.addWidget(self._body)

        lay.addStretch()

    def set_card(self, word: str, back_html: str, title: str = None):
        if title:
            self._title.setText(title)
        self._word.setText(word)
        self._body.setText(back_html)

    def clear(self):
        self._word.setText("")
        self._body.setText("")


# ─────────────────────────────────────────────────────────────
# WORKER THREADS
# ─────────────────────────────────────────────────────────────

def _get_front_word(note: dict) -> str:
    fields = note.get("fields", {})
    for name in ("Framsida", "Front", "Word", "Ord"):
        if name in fields:
            return BeautifulSoup(fields[name]["value"], "html.parser").get_text(strip=True)
    if fields:
        return BeautifulSoup(next(iter(fields.values()))["value"], "html.parser").get_text(strip=True)
    return ""


def _get_front(note: dict):
    """Returns (field_name, html)."""
    fields = note.get("fields", {})
    for name in ("Framsida", "Front", "Word", "Ord"):
        if name in fields:
            return name, fields[name]["value"]
    keys = list(fields.keys())
    if keys:
        return keys[0], fields[keys[0]]["value"]
    return "", ""


def _get_back(note: dict):
    """Returns (field_name, html)."""
    fields = note.get("fields", {})
    for name in ("Baksida", "Back", "Definition", "Förklaring", "Svar"):
        if name in fields:
            return name, fields[name]["value"]
    keys = list(fields.keys())
    if len(keys) > 1:
        return keys[1], fields[keys[1]]["value"]
    return "", ""


# ── Status badge on card front ──

_STATUS_BADGE_RE = re.compile(
    r'\s*<div id="swe-status"[^>]*>.*?</div>\s*',
    re.DOTALL | re.IGNORECASE,
)

_TAG_BADGE = {
    "swe_ok":        ("✓", "#2ea043"),
    "swe_mismatch":  ("✗", "#d29922"),
    "swe_not_found": ("?", "#f85149"),
    "swe_unclear":   ("~", "#7d8590"),
    "swe_updated":   ("★", "#a855f7"),
    "swe_created":   ("✦", "#3498db"),
}


def strip_status_badge(front_html: str) -> str:
    """Ta bort statusindikator från framsidan."""
    return _STATUS_BADGE_RE.sub("", front_html).strip()


# Vanliga generiska ord som INTE bör användas som fallback vid frassökning.
# Om "ha pippi på" inte hittas ska vi söka "pippi", inte "ha".
_GENERIC_WORDS = {
    "ha", "har", "hade", "haft",
    "göra", "gör", "gjorde", "gjort",
    "ta", "tar", "tog", "tagit",
    "ge", "ger", "gav", "gett", "givit",
    "gå", "går", "gick", "gått",
    "komma", "kommer", "kom", "kommit",
    "se", "ser", "såg", "sett",
    "bli", "blir", "blev", "blivit",
    "få", "får", "fick", "fått",
    "vara", "är", "var", "varit",
    "sätta", "sätter", "satte", "satt",
    "lägga", "lägger", "lade", "lagt",
    "ställa", "ställer", "ställde", "ställt",
    "stå", "står", "stod", "stått",
    "sitta", "sitter", "satt",
    "ligga", "ligger", "låg", "legat",
    "slå", "slår", "slog", "slagit",
    "dra", "drar", "drog", "dragit",
    "säga", "säger", "sade", "sagt",
    "köra", "kör", "körde", "kört",
    "låta", "låter", "lät", "låtit",
    "inte", "sig", "det", "den", "ett", "en",
    "med", "för", "till", "från", "på", "av", "om", "upp", "ut", "in",
}


def _best_phrase_word(phrase: str) -> str | None:
    """Hitta det mest specifika ordet i en fras att söka på."""
    words = phrase.split()
    # Returnera det första ordet som INTE är generiskt
    candidates = [w for w in words if w.lower() not in _GENERIC_WORDS and len(w) > 2]
    return candidates[0] if candidates else None


def add_status_badge(front_html: str, tag: str) -> str:
    """Lägg till en liten färgad status-prick på framsidan."""
    clean = strip_status_badge(front_html)
    symbol, color = _TAG_BADGE.get(tag, ("·", "#7d8590"))
    badge = (
        f'\n<div id="swe-status" style="font-size:16px; font-family:sans-serif; '
        f'margin-top:12px; color:{color}; text-align:left;">'
        f'{symbol}</div>'
    )
    return clean + badge


class ScanWorker(QThread):
    progress = Signal(int, int, str)        # current, total, word
    card_done = Signal(dict)                # result dict per card
    finished = Signal(dict)                 # final stats
    log = Signal(str)                       # log message

    def __init__(self, notes, threshold):
        super().__init__()
        self.notes = notes
        self.threshold = threshold
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        stats = {"ok": 0, "mismatch": 0, "not_found": 0, "unclear": 0, "error": 0}
        total = len(self.notes)

        with scraper_mod.SvenskaScraper() as svenska:
            for i, note in enumerate(self.notes):
                if self._cancel:
                    self.log.emit("Avbruten av användaren.")
                    break

                word = _get_front_word(note)
                _, back_html = _get_back(note)
                self.progress.emit(i, total, word)

                if not word:
                    stats["error"] += 1
                    continue

                try:
                    # Sök på Svenska.se
                    sv = svenska.search(word)
                    # Fraser: sök INTE enskilda ord — Svenska.se ger fel definition
                    # för idiom. Synonymer.se hanterar fraser bättre.

                    # Hämta synonymer från synonymer.se (söker hela frasen)
                    syn_text = synonymer_scraper.fetch_synonymer(word)

                    result = comparator.compare(
                        back_html, sv, self.threshold, synonymer_text=syn_text
                    )
                    tag = result["tag"]
                    key = tag.replace("swe_", "")
                    stats[key] = stats.get(key, 0) + 1

                    nid = note["noteId"]
                    anki_connect.remove_tags([nid], " ".join(
                        ["swe_ok", "swe_mismatch", "swe_not_found", "swe_unclear", "swe_updated"]))
                    anki_connect.add_tags([nid], tag)

                    self.card_done.emit({
                        "word": word, "tag": tag,
                        "score": result["score"], "note_id": nid,
                    })

                except Exception as e:
                    stats["error"] += 1
                    self.log.emit(f"Fel: {word} — {e}")

        synonymer_scraper.flush_cache()
        self.finished.emit(stats)


class UpdateWorker(QThread):
    progress = Signal(int, int, str)
    card_done = Signal(dict)                # word, old_html, new_html, note_id
    finished = Signal(dict)
    log = Signal(str)

    def __init__(self, notes, model, dry_run=False):
        super().__init__()
        self.notes = notes
        self.model = model
        self.dry_run = dry_run
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        stats = {"updated": 0, "not_found": 0, "error": 0}
        total = len(self.notes)
        all_tags = ["swe_ok", "swe_mismatch", "swe_not_found", "swe_unclear", "swe_updated"]

        # Spara backup INNAN vi ändrar något
        if not self.dry_run:
            self.log.emit("Skapar backup...")
            backup = []
            for note in self.notes:
                word = _get_front_word(note)
                field_name, old_html = _get_back(note)
                backup.append({
                    "note_id": note["noteId"],
                    "word": word,
                    "field_name": field_name,
                    "original_html": old_html,
                    "tags": note.get("tags", []),
                })
            ts = time.strftime("%Y%m%d_%H%M%S")
            backup_path = Path(f"backup_{ts}.json")
            backup_path.write_text(
                json.dumps(backup, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            self.log.emit(f"Backup sparad: {backup_path}")

        with scraper_mod.SvenskaScraper() as svenska:
            for i, note in enumerate(self.notes):
                if self._cancel:
                    self.log.emit("Avbruten.")
                    break

                word = _get_front_word(note)
                field_name, old_html = _get_back(note)
                nid = note["noteId"]
                self.progress.emit(i, total, word)

                if not word or not field_name:
                    stats["error"] += 1
                    continue

                try:
                    sv = svenska.search(word)
                    if not sv.get("found"):
                        stats["not_found"] += 1
                        if not self.dry_run:
                            anki_connect.remove_tags([nid], " ".join(all_tags))
                            anki_connect.add_tags([nid], "swe_not_found")
                        self.log.emit(f"Ej hittat: {word}")
                        continue

                    syn = synonymer_scraper.fetch_synonymer(word)
                    data = updater.extract_card_content(word, sv["text"], syn, self.model)
                    new_html = updater.build_card_back(word, data)

                    if not self.dry_run:
                        anki_connect.update_note_fields(nid, {field_name: new_html})
                        anki_connect.remove_tags([nid], " ".join(all_tags))
                        anki_connect.add_tags([nid], "swe_updated")

                    stats["updated"] += 1
                    self.card_done.emit({
                        "word": word, "old_html": old_html,
                        "new_html": new_html, "note_id": nid,
                    })

                except Exception as e:
                    stats["error"] += 1
                    self.log.emit(f"Fel: {word} — {e}")

        synonymer_scraper.flush_cache()
        self.finished.emit(stats)


# ─────────────────────────────────────────────────────────────
# CREATOR WORKER
# ─────────────────────────────────────────────────────────────

class CreatorWorker(QThread):
    """Genererar och skapar nya Anki-kort."""
    progress = Signal(int, int, str)
    card_done = Signal(dict)           # word, html
    finished = Signal(dict)            # stats
    log = Signal(str)
    words_ready = Signal(list)         # list of words from AI

    def __init__(self, words, deck_name, model_name, note_model, field_front, field_back, ai_model):
        super().__init__()
        self.words = words
        self.deck_name = deck_name
        self.model_name = note_model
        self.field_front = field_front
        self.field_back = field_back
        self.ai_model = ai_model
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        stats = {"created": 0, "skipped": 0, "error": 0}
        total = len(self.words)

        # Skapa decket om det inte finns
        try:
            anki_connect.create_deck(self.deck_name)
            self.log.emit(f"Deck: {self.deck_name}")
        except Exception as e:
            self.log.emit(f"Deck-fel: {e}")

        with scraper_mod.SvenskaScraper() as svenska:
            for i, word in enumerate(self.words):
                if self._cancel:
                    self.log.emit("Avbruten.")
                    break

                word = word.strip()
                if not word:
                    continue

                self.progress.emit(i, total, word)

                try:
                    # Skrapa Svenska.se
                    sv = svenska.search(word)
                    svenska_text = sv.get("text", "") if sv.get("found") else ""

                    # Skrapa synonymer.se
                    syn_text = synonymer_scraper.fetch_synonymer(word)

                    # AI genererar kortinnehåll
                    data = updater.extract_card_content(word, svenska_text, syn_text, self.ai_model)
                    back_html = updater.build_card_back(word, data)

                    # Framsida med styling (samma som McHP-formatet)
                    front_html = (
                        f'<div style="font-size:120px; font-family:Georgia, serif; '
                        f'font-style:italic; text-align:left;">{word}</div>'
                    )

                    # Skapa kortet i Anki
                    fields = {self.field_front: front_html, self.field_back: back_html}
                    try:
                        anki_connect.add_note(self.deck_name, self.model_name, fields, ["swe_created"])
                        stats["created"] += 1
                        self.card_done.emit({"word": word, "html": back_html})
                    except Exception as e:
                        if "duplicate" in str(e).lower():
                            stats["skipped"] += 1
                            self.log.emit(f"Duplikat: {word}")
                        else:
                            raise

                except Exception as e:
                    stats["error"] += 1
                    self.log.emit(f"Fel: {word} — {e}")

        synonymer_scraper.flush_cache()
        self.finished.emit(stats)


class WordGeneratorWorker(QThread):
    """Använder AI för att generera en ordlista baserat på ämne."""
    words_ready = Signal(list)
    log = Signal(str)

    def __init__(self, topic, count, ai_model):
        super().__init__()
        self.topic = topic
        self.count = count
        self.ai_model = ai_model

    def run(self):
        try:
            import ollama as _ollama
            prompt = (
                f"Skapa en lista med exakt {self.count} svenska ord inom ämnet \"{self.topic}\". "
                f"Orden ska vara varierande och intressanta, från grundläggande till avancerade. "
                f"Skriv ETT ord per rad, inget annat. Inga nummer, inga förklaringar, bara orden."
            )
            response = _ollama.chat(
                model=self.ai_model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.7},
            )
            raw = response["message"]["content"]
            words = [w.strip().strip("0123456789.-) ") for w in raw.strip().split("\n") if w.strip()]
            words = [w for w in words if w and len(w) > 1]
            self.words_ready.emit(words)
        except Exception as e:
            self.log.emit(f"AI-fel: {e}")
            self.words_ready.emit([])


# ─────────────────────────────────────────────────────────────
# STATS WORKER (background thread for dashboard stats)
# ─────────────────────────────────────────────────────────────

class StatsWorker(QThread):
    """Hämtar deck-statistik i bakgrundstråd så UI:t inte fryser."""
    stats_ready = Signal(dict)       # {"Totalt": n, "Korrekta": n, ...}
    error = Signal(str)

    def __init__(self, deck_name):
        super().__init__()
        self.deck_name = deck_name

    def run(self):
        try:
            ids = anki_connect.find_notes(self.deck_name)
            if not ids:
                self.stats_ready.emit({"Totalt": 0, "Korrekta": 0, "Mismatch": 0,
                                       "Ej hittade": 0, "Uppdaterade": 0})
                return

            # Räkna taggar via snabba findNotes-queries istället för att hämta alla notes
            deck_q = f'deck:"{self.deck_name}"'
            tag_map = {"swe_ok": "Korrekta", "swe_mismatch": "Mismatch",
                       "swe_not_found": "Ej hittade", "swe_updated": "Uppdaterade"}

            counts = {"Totalt": len(ids), "Korrekta": 0, "Mismatch": 0,
                      "Ej hittade": 0, "Uppdaterade": 0}
            for tag, key in tag_map.items():
                try:
                    tag_ids = anki_connect._request("findNotes", query=f'{deck_q} tag:{tag}')
                    counts[key] = len(tag_ids)
                except Exception:
                    pass

            self.stats_ready.emit(counts)

        except Exception as e:
            self.error.emit(str(e))


class InitWorker(QThread):
    """Kontrollerar Anki + Ollama i bakgrundstråd vid uppstart."""
    result = Signal(dict)

    def run(self):
        data = {"anki_ok": False, "decks": [], "ollama_ok": False, "models": [], "cache_count": 0}

        # Anki
        try:
            data["anki_ok"] = anki_connect.ping()
            if data["anki_ok"]:
                data["decks"] = anki_connect.get_deck_names()
        except Exception:
            pass

        # Ollama
        try:
            data["models"] = updater.list_models()
            data["ollama_ok"] = len(data["models"]) > 0
        except Exception:
            pass

        # Cache
        try:
            cache_path = Path("svenska_cache.json")
            if cache_path.exists():
                data["cache_count"] = len(json.loads(cache_path.read_text(encoding="utf-8")))
        except Exception:
            pass

        self.result.emit(data)


class NoteLoaderWorker(QThread):
    """Hämtar kort från Anki i bakgrundstråd."""
    notes_ready = Signal(list)      # filtered notes
    error = Signal(str)
    log = Signal(str)

    def __init__(self, deck_name, batch, skip_tags):
        super().__init__()
        self.deck_name = deck_name
        self.batch = batch
        self.skip_tags = skip_tags

    def run(self):
        try:
            ids = anki_connect.find_notes(self.deck_name)
            if not ids:
                self.notes_ready.emit([])
                return

            # Hämta kort i batcher om 100 — stoppa när vi har tillräckligt
            target = self.batch if self.batch > 0 else len(ids)
            filtered = []
            fetched = 0

            for i in range(0, len(ids), 100):
                batch_ids = ids[i:i + 100]
                batch_notes = anki_connect.get_notes_info(batch_ids)
                fetched += len(batch_notes)

                for n in batch_notes:
                    if self.skip_tags and any(t in n.get("tags", []) for t in self.skip_tags):
                        continue
                    filtered.append(n)
                    if len(filtered) >= target:
                        break

                self.log.emit(f"Hämtat {fetched} kort, {len(filtered)} kvar att bearbeta...")

                if len(filtered) >= target:
                    break

            self.notes_ready.emit(filtered)

        except Exception as e:
            self.error.emit(str(e))


# ─────────────────────────────────────────────────────────────
# DASHBOARD PAGE
# ─────────────────────────────────────────────────────────────

class DashboardPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win
        self._stats_worker = None
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(20)

        lay.addWidget(heading("Kontrollpanelen"))
        lay.addWidget(subtext("Översikt av ditt Anki-deck"))

        # Stats row
        self.stats_row = QHBoxLayout()
        self.stats_row.setSpacing(12)
        lay.addLayout(self.stats_row)

        self._badges = {}
        for label, color, bg in [
            ("Totalt", COLORS['accent'], COLORS['blue_bg']),
            ("Korrekta", COLORS['green'], COLORS['green_bg']),
            ("Mismatch", COLORS['yellow'], COLORS['yellow_bg']),
            ("Ej hittade", COLORS['red'], COLORS['red_bg']),
            ("Uppdaterade", "#a855f7", "#1e1232"),
        ]:
            frame, val_label = stat_badge(label, "—", color, bg)
            self._badges[label] = val_label
            self.stats_row.addWidget(frame)
        self.stats_row.addStretch()

        lay.addWidget(h_line())

        # Quick actions
        lay.addWidget(heading("Snabbåtgärder", 15))
        actions_row = QHBoxLayout()
        actions_row.setSpacing(12)

        btn_scan = QPushButton("  Skanna deck")
        btn_scan.setObjectName("accent")
        btn_scan.setFixedHeight(44)
        btn_scan.clicked.connect(lambda: main_win.navigate(1))
        actions_row.addWidget(btn_scan)

        btn_update = QPushButton("  Uppdatera med AI")
        btn_update.setFixedHeight(44)
        btn_update.clicked.connect(lambda: main_win.navigate(2))
        actions_row.addWidget(btn_update)

        btn_browse = QPushButton("  Bläddra kort")
        btn_browse.setFixedHeight(44)
        btn_browse.clicked.connect(lambda: main_win.navigate(3))
        actions_row.addWidget(btn_browse)

        actions_row.addStretch()
        lay.addLayout(actions_row)

        lay.addWidget(h_line())

        # Connection status
        self.status_frame = make_card()
        sf_lay = QVBoxLayout(self.status_frame)
        sf_lay.setContentsMargins(16, 12, 16, 12)
        self.status_label = QLabel("Kontrollerar anslutningar...")
        self.status_label.setStyleSheet(f"background: transparent; color: {COLORS['subtext']};")
        self.status_label.setWordWrap(True)
        sf_lay.addWidget(self.status_label)
        lay.addWidget(self.status_frame)

        lay.addStretch()

    def refresh_stats(self, deck_name):
        """Hämta statistik i bakgrundstråd — fryser INTE UI:t."""
        if not deck_name:
            return
        # Avbryt pågående hämtning
        if self._stats_worker and self._stats_worker.isRunning():
            return  # Redan igång, skippa
        self.status_label.setText("Hämtar statistik...")
        self._stats_worker = StatsWorker(deck_name)
        self._stats_worker.stats_ready.connect(self._on_stats_ready)
        self._stats_worker.error.connect(self._on_stats_error)
        self._stats_worker.start()

    def _on_stats_ready(self, counts):
        for label, badge_label in self._badges.items():
            badge_label.setText(str(counts.get(label, 0)))
        self.status_label.setText("")

    def _on_stats_error(self, msg):
        self.status_label.setText(f"Kunde inte hämta statistik: {msg}")

    def update_status(self, anki_ok, ollama_ok, model_name, cache_count):
        parts = []
        parts.append(f"{'✓' if anki_ok else '✗'} Anki {'ansluten' if anki_ok else 'ej ansluten'}")
        parts.append(f"{'✓' if ollama_ok else '✗'} Ollama {'igång' if ollama_ok else 'ej igång'} ({model_name})")
        parts.append(f"Cache: {cache_count} ord")
        self.status_label.setText("   |   ".join(parts))


# ─────────────────────────────────────────────────────────────
# SCANNER PAGE
# ─────────────────────────────────────────────────────────────

class ScannerPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win
        self.worker = None
        self._start_time = 0

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(16)

        lay.addWidget(heading("Skanna mot Svenska.se"))
        lay.addWidget(subtext("Kontrollera om kortens förklaringar stämmer med SAOL, SO och SAOB"))

        # Controls
        ctrl = QHBoxLayout()
        ctrl.setSpacing(12)

        ctrl.addWidget(QLabel("Antal kort:"))
        self.batch_spin = QSpinBox()
        self.batch_spin.setRange(0, 50000)
        self.batch_spin.setValue(100)
        self.batch_spin.setSpecialValueText("Alla")
        self.batch_spin.setFixedWidth(100)
        ctrl.addWidget(self.batch_spin)

        ctrl.addWidget(QLabel("Tröskel:"))
        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setRange(5, 50)
        self.threshold_slider.setValue(25)
        self.threshold_slider.setFixedWidth(150)
        ctrl.addWidget(self.threshold_slider)
        self.threshold_label = QLabel("0.25")
        self.threshold_label.setFixedWidth(35)
        ctrl.addWidget(self.threshold_label)
        self.threshold_slider.valueChanged.connect(
            lambda v: self.threshold_label.setText(f"{v/100:.2f}"))

        ctrl.addStretch()

        self.btn_start = QPushButton("  Starta skanning")
        self.btn_start.setObjectName("accent")
        self.btn_start.setFixedHeight(40)
        self.btn_start.clicked.connect(self.start_scan)
        ctrl.addWidget(self.btn_start)

        self.btn_stop = QPushButton("  Stoppa")
        self.btn_stop.setObjectName("danger")
        self.btn_stop.setFixedHeight(40)
        self.btn_stop.setVisible(False)
        self.btn_stop.clicked.connect(self.stop_scan)
        ctrl.addWidget(self.btn_stop)

        lay.addLayout(ctrl)

        # Progress
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        lay.addWidget(self.progress)

        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet(f"color: {COLORS['subtext']}; background: transparent;")
        lay.addWidget(self.progress_label)

        # Results table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Ord", "Status", "Poäng", "Tagg"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        lay.addWidget(self.table)

        # Log
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(80)
        self.log.setPlaceholderText("Loggar visas här...")
        lay.addWidget(self.log)

    def start_scan(self):
        deck = self.main.current_deck()
        if not deck:
            return

        self.table.setRowCount(0)
        self.log.clear()
        self.btn_start.setEnabled(False)
        self.progress_label.setText("Hämtar kort från Anki...")

        batch = self.batch_spin.value()
        self._threshold = self.threshold_slider.value() / 100
        skip_tags = ["swe_ok", "swe_mismatch", "swe_not_found", "swe_unclear", "swe_updated"]

        self._loader = NoteLoaderWorker(deck, batch, skip_tags)
        self._loader.notes_ready.connect(self._on_notes_loaded)
        self._loader.error.connect(lambda msg: (self.log.append(f"FEL: {msg}"),
                                                self.btn_start.setEnabled(True)))
        self._loader.log.connect(lambda msg: self.log.append(msg))
        self._loader.start()

    def _on_notes_loaded(self, notes):
        """Kallas när NoteLoaderWorker är klar — startar skanning."""
        self.btn_start.setEnabled(True)

        if not notes:
            self.log.append("Inga obearbetade kort hittades.")
            self.progress_label.setText("")
            return

        # Bekräfta stora körningar
        if len(notes) > 200:
            mins = len(notes) * 3 // 60
            reply = QMessageBox.question(
                self, "Stor körning",
                f"Skanna {len(notes)} kort?\nBeräknad tid: ~{mins} minuter.")
            if reply != QMessageBox.Yes:
                self.progress_label.setText("")
                return

        self._start_time = time.time()
        self.progress.setMaximum(len(notes))
        self.progress.setValue(0)
        self.progress.setVisible(True)
        self.btn_start.setVisible(False)
        self.btn_stop.setVisible(True)

        self.worker = ScanWorker(notes, self._threshold)
        self.worker.progress.connect(self._on_progress)
        self.worker.card_done.connect(self._on_card)
        self.worker.log.connect(lambda msg: self.log.append(msg))
        self.worker.finished.connect(self._on_done)
        self.worker.start()

    def stop_scan(self):
        if self.worker:
            self.worker.cancel()

    def _on_progress(self, i, total, word):
        self.progress.setValue(i + 1)
        eta = format_eta(self._start_time, i + 1, total)
        self.progress_label.setText(f"{i+1}/{total}  —  {word}  —  {eta}")

    def _on_card(self, result):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(result["word"]))

        tag = result["tag"]
        status_map = {"swe_ok": ("✓ Korrekt", COLORS['green']),
                      "swe_mismatch": ("✗ Mismatch", COLORS['yellow']),
                      "swe_not_found": ("— Ej hittat", COLORS['red']),
                      "swe_unclear": ("? Oklart", COLORS['subtext'])}
        text, color = status_map.get(tag, ("?", COLORS['subtext']))

        status_item = QTableWidgetItem(text)
        status_item.setForeground(QColor(color))
        self.table.setItem(row, 1, status_item)

        score_item = QTableWidgetItem(f"{result['score']:.2f}")
        self.table.setItem(row, 2, score_item)
        self.table.setItem(row, 3, QTableWidgetItem(tag))

        self.table.scrollToBottom()

    def _on_done(self, stats):
        self.btn_start.setVisible(True)
        self.btn_stop.setVisible(False)
        self.progress.setVisible(False)
        total = sum(stats.values())
        self.progress_label.setText(
            f"Klart! {total} kort  —  "
            f"✓ {stats.get('ok',0)}  ✗ {stats.get('mismatch',0)}  "
            f"— {stats.get('not_found',0)}  Fel: {stats.get('error',0)}"
        )
        self.main.dashboard.refresh_stats(self.main.current_deck())


# ─────────────────────────────────────────────────────────────
# UPDATER PAGE
# ─────────────────────────────────────────────────────────────

class UpdaterPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win
        self.worker = None
        self._start_time = 0

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(16)

        lay.addWidget(heading("Uppdatera med AI"))
        lay.addWidget(subtext("Lokal AI (Ollama) skriver om korten med data från Svenska.se + synonymer.se"))

        # Controls
        ctrl = QHBoxLayout()
        ctrl.setSpacing(12)

        ctrl.addWidget(QLabel("Antal kort:"))
        self.batch_spin = QSpinBox()
        self.batch_spin.setRange(0, 50000)
        self.batch_spin.setValue(20)
        self.batch_spin.setSpecialValueText("Alla")
        self.batch_spin.setFixedWidth(100)
        ctrl.addWidget(self.batch_spin)

        ctrl.addWidget(QLabel("Modell:"))
        self.model_combo = QComboBox()
        self.model_combo.setFixedWidth(160)
        ctrl.addWidget(self.model_combo)

        self.dry_run_check = QCheckBox("Dry run (ändra inget)")
        ctrl.addWidget(self.dry_run_check)

        ctrl.addStretch()

        self.btn_start = QPushButton("  Starta AI-uppdatering")
        self.btn_start.setObjectName("accent")
        self.btn_start.setFixedHeight(40)
        self.btn_start.clicked.connect(self.start_update)
        ctrl.addWidget(self.btn_start)

        self.btn_stop = QPushButton("  Stoppa")
        self.btn_stop.setObjectName("danger")
        self.btn_stop.setFixedHeight(40)
        self.btn_stop.setVisible(False)
        self.btn_stop.clicked.connect(self.stop_update)
        ctrl.addWidget(self.btn_stop)

        lay.addLayout(ctrl)

        # Progress
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        lay.addWidget(self.progress)

        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet(f"color: {COLORS['subtext']}; background: transparent;")
        lay.addWidget(self.progress_label)

        # Before / After preview
        preview_split = QHBoxLayout()
        preview_split.setSpacing(16)

        self.card_before = CardPreview("FÖRE")
        self.card_after = CardPreview("EFTER")
        preview_split.addWidget(self.card_before)
        preview_split.addWidget(self.card_after)
        lay.addLayout(preview_split)

        # Log
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(100)
        self.log.setPlaceholderText("Loggar visas här...")
        lay.addWidget(self.log)

    def refresh_models(self):
        self.model_combo.clear()
        models = updater.list_models()
        if models:
            self.model_combo.addItems(models)
            if "mistral:latest" in models:
                self.model_combo.setCurrentText("mistral:latest")
            elif "mistral" in models:
                self.model_combo.setCurrentText("mistral")
        else:
            self.model_combo.addItem("(Ollama ej igång)")

    def start_update(self):
        deck = self.main.current_deck()
        model = self.model_combo.currentText()
        if not deck or "(Ollama" in model:
            self.log.append("Välj ett deck och se till att Ollama är igång.")
            return

        batch = self.batch_spin.value()
        self._dry_run = self.dry_run_check.isChecked()
        self._model = model
        self.log.clear()
        self.btn_start.setEnabled(False)
        self.progress_label.setText("Hämtar kort från Anki...")

        skip_tags = ["swe_ok", "swe_updated"]
        self._loader = NoteLoaderWorker(deck, batch, skip_tags)
        self._loader.notes_ready.connect(self._on_notes_loaded)
        self._loader.error.connect(lambda msg: (self.log.append(f"FEL: {msg}"),
                                                self.btn_start.setEnabled(True)))
        self._loader.log.connect(lambda msg: self.log.append(msg))
        self._loader.start()

    def _on_notes_loaded(self, notes):
        """Kallas när NoteLoaderWorker är klar — startar AI-uppdatering."""
        self.btn_start.setEnabled(True)

        if not notes:
            self.log.append("Inga kort att uppdatera (alla är swe_ok eller swe_updated).")
            self.progress_label.setText("")
            return

        # Bekräfta stora körningar
        if len(notes) > 50 and not self._dry_run:
            reply = QMessageBox.question(
                self, "Stor uppdatering",
                f"Uppdatera {len(notes)} kort med AI?\n"
                f"En backup skapas automatiskt.")
            if reply != QMessageBox.Yes:
                self.progress_label.setText("")
                return

        self._start_time = time.time()
        self.progress.setMaximum(len(notes))
        self.progress.setValue(0)
        self.progress.setVisible(True)
        self.btn_start.setVisible(False)
        self.btn_stop.setVisible(True)

        self.worker = UpdateWorker(notes, self._model, self._dry_run)
        self.worker.progress.connect(self._on_progress)
        self.worker.card_done.connect(self._on_card)
        self.worker.log.connect(lambda msg: self.log.append(msg))
        self.worker.finished.connect(self._on_done)
        self.worker.start()

    def stop_update(self):
        if self.worker:
            self.worker.cancel()

    def _on_progress(self, i, total, word):
        self.progress.setValue(i + 1)
        eta = format_eta(self._start_time, i + 1, total)
        self.progress_label.setText(f"{i+1}/{total}  —  {word}  —  {eta}")

    def _on_card(self, result):
        word = result["word"]
        self.card_before.set_card(word, result["old_html"], "FÖRE")
        self.card_after.set_card(word, result["new_html"], "EFTER")
        self.log.append(f"✓ {word}")

    def _on_done(self, stats):
        self.btn_start.setVisible(True)
        self.btn_stop.setVisible(False)
        self.progress.setVisible(False)
        self.progress_label.setText(
            f"Klart!  Uppdaterade: {stats['updated']}  |  "
            f"Ej hittade: {stats['not_found']}  |  Fel: {stats['error']}"
        )
        self.main.dashboard.refresh_stats(self.main.current_deck())


# ─────────────────────────────────────────────────────────────
# BROWSER PAGE
# ─────────────────────────────────────────────────────────────

class BrowserPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win
        self._notes = []
        self._filtered_rows = []  # maps table row → note

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(10)

        lay.addWidget(heading("Kortläsare"))

        # ── Row 1: Filter + Search + Load ──
        row1 = QHBoxLayout()
        row1.setSpacing(10)

        row1.addWidget(QLabel("Filter:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Alla", "swe_ok", "swe_mismatch", "swe_not_found", "swe_updated", "swe_created", "Otaggade"])
        self.filter_combo.setFixedWidth(150)
        self.filter_combo.currentTextChanged.connect(self._apply_filters)
        row1.addWidget(self.filter_combo)

        row1.addWidget(QLabel("Sök:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Sök ord...")
        self.search_input.setFixedWidth(200)
        self.search_input.setStyleSheet(f"""
            QLineEdit {{
                background: {COLORS['card']};
                border: 1px solid {COLORS['border']};
                border-radius: 6px;
                padding: 6px 10px;
            }}
            QLineEdit:focus {{
                border-color: {COLORS['accent']};
            }}
        """)
        self.search_input.textChanged.connect(self._apply_filters)
        row1.addWidget(self.search_input)

        self.btn_load = QPushButton("  Ladda kort")
        self.btn_load.setObjectName("accent")
        self.btn_load.clicked.connect(self.load_cards)
        row1.addWidget(self.btn_load)

        self.count_label = subtext("")
        row1.addWidget(self.count_label)
        row1.addStretch()
        lay.addLayout(row1)

        # ── Row 2: Bulk tag operations ──
        row2 = QHBoxLayout()
        row2.setSpacing(8)

        row2.addWidget(subtext("Markera valda som:"))
        for tag_name, label, color in [
            ("swe_ok", "✓ Korrekt", COLORS['green']),
            ("swe_mismatch", "✗ Mismatch", COLORS['yellow']),
        ]:
            btn = QPushButton(label)
            btn.setFixedHeight(30)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: transparent;
                    border: 1px solid {color};
                    color: {color};
                    border-radius: 6px;
                    padding: 2px 10px;
                    font-size: 12px;
                }}
                QPushButton:hover {{ background: {color}; color: white; }}
            """)
            btn.clicked.connect(lambda checked, t=tag_name: self._bulk_tag(t))
            row2.addWidget(btn)

        btn_remove = QPushButton("  Ta bort taggar")
        btn_remove.setFixedHeight(30)
        btn_remove.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                border: 1px solid {COLORS['subtext']};
                color: {COLORS['subtext']};
                border-radius: 6px;
                padding: 2px 10px;
                font-size: 12px;
            }}
            QPushButton:hover {{ background: {COLORS['border']}; }}
        """)
        btn_remove.clicked.connect(lambda: self._bulk_tag(None))
        row2.addWidget(btn_remove)

        row2.addStretch()

        self.btn_export = QPushButton("  Exportera CSV")
        self.btn_export.setFixedHeight(30)
        self.btn_export.clicked.connect(self.export_csv)
        row2.addWidget(self.btn_export)

        lay.addLayout(row2)

        # ── Splitter: table + preview ──
        splitter = QSplitter(Qt.Horizontal)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Ord", "Tagg", "ID"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.table.setColumnWidth(2, 0)  # Dölj ID-kolumnen visuellt
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.ExtendedSelection)  # Multi-select
        self.table.currentCellChanged.connect(self._on_select)
        splitter.addWidget(self.table)

        self.preview = CardPreview("Förhandsvisning")
        self.preview.setMinimumWidth(300)
        splitter.addWidget(self.preview)

        splitter.setSizes([500, 400])
        lay.addWidget(splitter)

    def load_cards(self):
        deck = self.main.current_deck()
        if not deck:
            return

        self.btn_load.setEnabled(False)
        self.count_label.setText("Laddar kort...")

        self._browser_loader = NoteLoaderWorker(deck, 0, [])  # 0 = alla, [] = inga skip-tags
        self._browser_loader.notes_ready.connect(self._on_browser_loaded)
        self._browser_loader.error.connect(lambda msg: (
            QMessageBox.warning(self, "Fel", f"Kunde inte ladda kort: {msg}"),
            self.btn_load.setEnabled(True),
            self.count_label.setText(""),
        ))
        self._browser_loader.start()

    def _on_browser_loaded(self, notes):
        self.btn_load.setEnabled(True)
        self._notes = notes
        self._apply_filters()

    def _apply_filters(self):
        """Filtrera tabell baserat på tagg-filter och söktext."""
        filt = self.filter_combo.currentText()
        search = self.search_input.text().strip().lower()
        swe_tags = ["swe_ok", "swe_mismatch", "swe_not_found", "swe_updated", "swe_created"]

        self.table.setRowCount(0)
        self._filtered_rows = []

        for note in self._notes:
            tags = note.get("tags", [])
            tag_found = next((t for t in swe_tags if t in tags), None)
            tag_str = tag_found or "—"

            # Tagg-filter
            if filt == "Alla":
                pass
            elif filt == "Otaggade":
                if tag_found:
                    continue
            elif filt != tag_str:
                continue

            word = _get_front_word(note)

            # Sök-filter
            if search and search not in word.lower():
                continue

            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(word))

            tag_item = QTableWidgetItem(tag_str)
            color_map = {"swe_ok": COLORS['green'], "swe_mismatch": COLORS['yellow'],
                         "swe_not_found": COLORS['red'], "swe_updated": "#a855f7",
                         "swe_created": COLORS['accent']}
            if tag_str in color_map:
                tag_item.setForeground(QColor(color_map[tag_str]))
            self.table.setItem(row, 1, tag_item)
            self.table.setItem(row, 2, QTableWidgetItem(str(note["noteId"])))
            self._filtered_rows.append(note)

        self.count_label.setText(f"{self.table.rowCount()} kort")

    def _on_select(self, row, col, prev_row, prev_col):
        if row < 0 or row >= len(self._filtered_rows):
            return
        note = self._filtered_rows[row]
        word = _get_front_word(note)
        _, back = _get_back(note)
        self.preview.set_card(word, back)

    def _bulk_tag(self, new_tag):
        """Tagga alla markerade rader med new_tag (None = ta bort alla swe-taggar)."""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.information(self, "Ingen markering", "Markera rader i tabellen först (Ctrl+klick eller Shift+klick).")
            return

        all_tags = "swe_ok swe_mismatch swe_not_found swe_unclear swe_updated swe_created"
        count = len(selected)
        action = f"tagga {count} kort som {new_tag}" if new_tag else f"ta bort taggar från {count} kort"

        reply = QMessageBox.question(self, "Bekräfta", f"Vill du {action}?")
        if reply != QMessageBox.Yes:
            return

        for idx in selected:
            row = idx.row()
            nid_item = self.table.item(row, 2)
            if not nid_item:
                continue
            nid = int(nid_item.text())
            try:
                anki_connect.remove_tags([nid], all_tags)
                if new_tag:
                    anki_connect.add_tags([nid], new_tag)
            except Exception:
                pass

        # Uppdatera tabellen
        self.load_cards()
        self.main.dashboard.refresh_stats(self.main.current_deck())

    def export_csv(self):
        path = Path("export_kort.csv")
        rows = []
        for r in range(self.table.rowCount()):
            word = self.table.item(r, 0).text() if self.table.item(r, 0) else ""
            tag = self.table.item(r, 1).text() if self.table.item(r, 1) else ""
            rows.append(f"{word},{tag}")
        path.write_text("Ord,Tagg\n" + "\n".join(rows), encoding="utf-8")
        QMessageBox.information(self, "Export", f"Exporterat {len(rows)} kort till {path}")


# ─────────────────────────────────────────────────────────────
# SETTINGS PAGE
# ─────────────────────────────────────────────────────────────

class SettingsPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(20)

        lay.addWidget(heading("Inställningar"))

        # Ollama
        card1 = make_card()
        c1 = QVBoxLayout(card1)
        c1.setContentsMargins(20, 16, 20, 16)
        c1.addWidget(heading("AI-modell (Ollama)", 14))
        c1.addWidget(subtext("Modellen som används för att generera kortinnehåll"))

        row1 = QHBoxLayout()
        self.model_combo = QComboBox()
        self.model_combo.setFixedWidth(200)
        row1.addWidget(self.model_combo)
        self.btn_refresh = QPushButton("Uppdatera lista")
        self.btn_refresh.clicked.connect(self.refresh_models)
        row1.addWidget(self.btn_refresh)
        row1.addStretch()
        c1.addLayout(row1)
        lay.addWidget(card1)

        # Cache
        card2 = make_card()
        c2 = QVBoxLayout(card2)
        c2.setContentsMargins(20, 16, 20, 16)
        c2.addWidget(heading("Cache", 14))
        self.cache_label = subtext("Laddar...")
        c2.addWidget(self.cache_label)

        cache_row = QHBoxLayout()
        self.btn_clear = QPushButton("Rensa cache")
        self.btn_clear.setObjectName("danger")
        self.btn_clear.clicked.connect(self.clear_cache)
        cache_row.addWidget(self.btn_clear)
        cache_row.addStretch()
        c2.addLayout(cache_row)
        lay.addWidget(card2)

        # Backup / Restore
        card3 = make_card()
        c3 = QVBoxLayout(card3)
        c3.setContentsMargins(20, 16, 20, 16)
        c3.addWidget(heading("Backup & återställning", 14))
        c3.addWidget(subtext("Backups skapas automatiskt innan varje AI-uppdatering"))

        self.backup_combo = QComboBox()
        self.backup_combo.setFixedWidth(300)
        c3.addWidget(self.backup_combo)

        restore_row = QHBoxLayout()
        self.btn_restore = QPushButton("  Återställ vald backup")
        self.btn_restore.setObjectName("danger")
        self.btn_restore.clicked.connect(self.restore_backup)
        restore_row.addWidget(self.btn_restore)

        self.btn_refresh_backups = QPushButton("Uppdatera lista")
        self.btn_refresh_backups.clicked.connect(self.refresh_backups)
        restore_row.addWidget(self.btn_refresh_backups)
        restore_row.addStretch()
        c3.addLayout(restore_row)
        lay.addWidget(card3)

        # Tags management
        card4 = make_card()
        c4 = QVBoxLayout(card4)
        c4.setContentsMargins(20, 16, 20, 16)
        c4.addWidget(heading("Taggar", 14))
        c4.addWidget(subtext("Ta bort alla swe_*-taggar för att köra om skanningen"))

        self.btn_clear_tags = QPushButton("  Rensa alla swe-taggar från decket")
        self.btn_clear_tags.setObjectName("danger")
        self.btn_clear_tags.clicked.connect(self.clear_tags)
        c4.addWidget(self.btn_clear_tags)
        lay.addWidget(card4)

        lay.addStretch()

    def refresh_models(self):
        self.model_combo.clear()
        models = updater.list_models()
        self.model_combo.addItems(models if models else ["(Ollama ej igång)"])

    def refresh_cache(self):
        parts = []
        sv_path = Path("svenska_cache.json")
        if sv_path.exists():
            sv_cache = json.loads(sv_path.read_text(encoding="utf-8"))
            parts.append(f"Svenska.se: {len(sv_cache)} ord ({sv_path.stat().st_size // 1024} KB)")
        syn_path = Path("synonymer_cache.json")
        if syn_path.exists():
            syn_cache = json.loads(syn_path.read_text(encoding="utf-8"))
            parts.append(f"Synonymer.se: {len(syn_cache)} ord ({syn_path.stat().st_size // 1024} KB)")
        if parts:
            self.cache_label.setText("  |  ".join(parts))
        else:
            self.cache_label.setText("Ingen cache-fil hittad.")

    def clear_cache(self):
        reply = QMessageBox.question(
            self, "Rensa cache", "Vill du verkligen radera all cachad data från Svenska.se och synonymer.se?")
        if reply == QMessageBox.Yes:
            Path("svenska_cache.json").unlink(missing_ok=True)
            Path("synonymer_cache.json").unlink(missing_ok=True)
            # Nollställ in-memory cache
            synonymer_scraper._cache = None
            self.refresh_cache()

    def refresh_backups(self):
        self.backup_combo.clear()
        backups = sorted(Path(".").glob("backup_*.json"), reverse=True)
        if backups:
            for b in backups:
                size = b.stat().st_size // 1024
                data = json.loads(b.read_text(encoding="utf-8"))
                self.backup_combo.addItem(f"{b.name}  ({len(data)} kort, {size} KB)", str(b))
        else:
            self.backup_combo.addItem("(Inga backups hittade)")

    def restore_backup(self):
        path_str = self.backup_combo.currentData()
        if not path_str:
            return
        path = Path(path_str)
        if not path.exists():
            QMessageBox.warning(self, "Fel", "Backup-filen hittades inte.")
            return

        reply = QMessageBox.question(
            self, "Återställ backup",
            f"Återställa {path.name}?\n\nDetta skriver tillbaka ORIGINALINNEHÅLL till alla kort i backupen.")
        if reply != QMessageBox.Yes:
            return

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            restored = 0
            all_tags = "swe_ok swe_mismatch swe_not_found swe_unclear swe_updated swe_created"
            for entry in data:
                nid = entry["note_id"]
                field = entry["field_name"]
                html = entry["original_html"]
                anki_connect.update_note_fields(nid, {field: html})
                anki_connect.remove_tags([nid], all_tags)

                # Ta bort statusbadge från framsidan
                try:
                    note_info = anki_connect.get_notes_info([nid])
                    if note_info:
                        front_field, front_html = _get_front(note_info[0])
                        if front_field and '<div id="swe-status"' in front_html:
                            anki_connect.update_note_fields(nid, {front_field: strip_status_badge(front_html)})
                except Exception:
                    pass

                restored += 1

            QMessageBox.information(
                self, "Klart", f"Återställde {restored} kort till originalinnehåll.")
        except Exception as e:
            QMessageBox.warning(self, "Fel", f"Kunde inte återställa: {e}")

    def clear_tags(self):
        deck = self.main.current_deck()
        if not deck:
            return
        reply = QMessageBox.question(
            self, "Rensa taggar",
            f"Ta bort ALLA swe_*-taggar och statusmarkeringar från '{deck}'?")
        if reply == QMessageBox.Yes:
            try:
                ids = anki_connect.find_notes(deck)
                all_tags = "swe_ok swe_mismatch swe_not_found swe_unclear swe_updated swe_created"

                notes = []
                for i in range(0, len(ids), 100):
                    batch = anki_connect.get_notes_info(ids[i:i + 100])
                    anki_connect.remove_tags(ids[i:i + 100], all_tags)
                    notes.extend(batch)

                # Ta bort statusbadges från framsidan
                cleaned = 0
                for note in notes:
                    front_field, front_html = _get_front(note)
                    if front_field and '<div id="swe-status"' in front_html:
                        new_front = strip_status_badge(front_html)
                        anki_connect.update_note_fields(note["noteId"], {front_field: new_front})
                        cleaned += 1

                msg = f"Taggar borttagna från {len(ids)} kort."
                if cleaned:
                    msg += f"\nStatusmarkeringar borttagna från {cleaned} kort."
                QMessageBox.information(self, "Klart", msg)
            except Exception as e:
                QMessageBox.warning(self, "Fel", str(e))


# ─────────────────────────────────────────────────────────────
# CREATOR PAGE
# ─────────────────────────────────────────────────────────────

class CreatorPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main = main_win
        self.worker = None
        self.gen_worker = None
        self._start_time = 0

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(14)

        lay.addWidget(heading("Skapa nytt deck"))
        lay.addWidget(subtext("Generera Anki-kort med AI, Svenska.se och synonymer.se"))

        # ── Deck-info ──
        info_card = make_card()
        info_lay = QVBoxLayout(info_card)
        info_lay.setContentsMargins(16, 12, 16, 12)

        row_deck = QHBoxLayout()
        row_deck.addWidget(QLabel("Deck-namn:"))
        self.deck_input = QComboBox()
        self.deck_input.setEditable(True)
        self.deck_input.setFixedWidth(280)
        self.deck_input.setPlaceholderText("t.ex. Svenska::Medicin")
        row_deck.addWidget(self.deck_input)

        row_deck.addSpacing(20)
        row_deck.addWidget(QLabel("Korttyp:"))
        self.model_combo = QComboBox()
        self.model_combo.setFixedWidth(200)
        self.model_combo.currentTextChanged.connect(self._on_model_change)
        row_deck.addWidget(self.model_combo)
        row_deck.addStretch()
        info_lay.addLayout(row_deck)

        row_fields = QHBoxLayout()
        row_fields.addWidget(QLabel("Framsida-fält:"))
        self.field_front_combo = QComboBox()
        self.field_front_combo.setFixedWidth(140)
        row_fields.addWidget(self.field_front_combo)
        row_fields.addSpacing(12)
        row_fields.addWidget(QLabel("Baksida-fält:"))
        self.field_back_combo = QComboBox()
        self.field_back_combo.setFixedWidth(140)
        row_fields.addWidget(self.field_back_combo)
        row_fields.addStretch()
        info_lay.addLayout(row_fields)

        lay.addWidget(info_card)

        # ── AI-ordgenerator ──
        gen_card = make_card()
        gen_lay = QVBoxLayout(gen_card)
        gen_lay.setContentsMargins(16, 12, 16, 12)
        gen_lay.addWidget(heading("Generera ordlista med AI", 13))

        gen_row = QHBoxLayout()
        gen_row.addWidget(QLabel("Ämne:"))
        self.topic_input = QComboBox()
        self.topic_input.setEditable(True)
        self.topic_input.setFixedWidth(240)
        self.topic_input.addItems([
            "", "Vardagliga verb", "Akademiska ord", "Medicinska termer",
            "Juridiska termer", "Känslor och sinnesstämningar", "Natur och djur",
            "Mat och matlagning", "Ovanliga svenska ord", "Affärssvenska",
        ])
        gen_row.addWidget(self.topic_input)

        gen_row.addWidget(QLabel("Antal:"))
        self.gen_count = QSpinBox()
        self.gen_count.setRange(5, 200)
        self.gen_count.setValue(20)
        self.gen_count.setFixedWidth(80)
        gen_row.addWidget(self.gen_count)

        self.btn_generate = QPushButton("  Generera ordlista")
        self.btn_generate.clicked.connect(self.generate_words)
        gen_row.addWidget(self.btn_generate)
        gen_row.addStretch()
        gen_lay.addLayout(gen_row)

        lay.addWidget(gen_card)

        # ── Ordlista ──
        words_row = QHBoxLayout()

        words_left = QVBoxLayout()
        words_left.addWidget(QLabel("Ord att skapa (ett per rad):"))
        self.word_input = QTextEdit()
        self.word_input.setPlaceholderText("springa\nbeprövad\nknata\n...")
        self.word_input.setMinimumHeight(140)
        words_left.addWidget(self.word_input)

        word_count_row = QHBoxLayout()
        self.word_count_label = subtext("0 ord")
        word_count_row.addWidget(self.word_count_label)
        word_count_row.addStretch()
        words_left.addLayout(word_count_row)

        words_row.addLayout(words_left)

        # Preview
        self.preview = CardPreview("Förhandsvisning")
        self.preview.setMinimumWidth(320)
        words_row.addWidget(self.preview)

        lay.addLayout(words_row)

        self.word_input.textChanged.connect(self._update_word_count)

        # ── Kontroller ──
        ctrl = QHBoxLayout()

        self.btn_ai_model = QComboBox()
        self.btn_ai_model.setFixedWidth(160)
        ctrl.addWidget(QLabel("AI-modell:"))
        ctrl.addWidget(self.btn_ai_model)

        ctrl.addStretch()

        self.btn_start = QPushButton("  Skapa kort i Anki")
        self.btn_start.setObjectName("accent")
        self.btn_start.setFixedHeight(42)
        self.btn_start.setFixedWidth(200)
        self.btn_start.clicked.connect(self.start_creation)
        ctrl.addWidget(self.btn_start)

        self.btn_stop = QPushButton("  Stoppa")
        self.btn_stop.setObjectName("danger")
        self.btn_stop.setFixedHeight(42)
        self.btn_stop.setVisible(False)
        self.btn_stop.clicked.connect(self.stop_creation)
        ctrl.addWidget(self.btn_stop)

        lay.addLayout(ctrl)

        # Progress + log
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        lay.addWidget(self.progress)

        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet(f"color: {COLORS['subtext']}; background: transparent;")
        lay.addWidget(self.progress_label)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(70)
        self.log.setPlaceholderText("Loggar visas här...")
        lay.addWidget(self.log)

    def refresh_models(self):
        """Ladda Anki-korttyper och Ollama-modeller."""
        # Anki note models
        self.model_combo.clear()
        try:
            models = anki_connect.model_names()
            self.model_combo.addItems(models)
        except Exception:
            self.model_combo.addItem("(Anki ej ansluten)")

        # Existing decks for combo
        self.deck_input.clear()
        try:
            decks = anki_connect.get_deck_names()
            self.deck_input.addItems(sorted(decks))
            self.deck_input.setCurrentText("")
        except Exception:
            pass

        # Ollama models
        self.btn_ai_model.clear()
        ai_models = updater.list_models()
        self.btn_ai_model.addItems(ai_models if ai_models else ["(Ollama ej igång)"])
        if "mistral:latest" in (ai_models or []):
            self.btn_ai_model.setCurrentText("mistral:latest")

    def _on_model_change(self, model_name):
        """Uppdatera fält-combos när korttyp ändras."""
        self.field_front_combo.clear()
        self.field_back_combo.clear()
        if not model_name or model_name.startswith("("):
            return
        try:
            fields = anki_connect.model_field_names(model_name)
            self.field_front_combo.addItems(fields)
            self.field_back_combo.addItems(fields)
            # Gissa rätt fält
            for i, f in enumerate(fields):
                if f.lower() in ("framsida", "front", "word", "fråga"):
                    self.field_front_combo.setCurrentIndex(i)
                if f.lower() in ("baksida", "back", "definition", "svar"):
                    self.field_back_combo.setCurrentIndex(i)
            # Om inget matchade, ta andra fältet som back
            if len(fields) > 1 and self.field_back_combo.currentIndex() == self.field_front_combo.currentIndex():
                self.field_back_combo.setCurrentIndex(1)
        except Exception:
            pass

    def _update_word_count(self):
        words = [w.strip() for w in self.word_input.toPlainText().strip().split("\n") if w.strip()]
        self.word_count_label.setText(f"{len(words)} ord")

    def generate_words(self):
        topic = self.topic_input.currentText().strip()
        if not topic:
            self.log.append("Skriv in ett ämne först.")
            return
        ai = self.btn_ai_model.currentText()
        if not ai or ai.startswith("("):
            self.log.append("Ollama behöver vara igång.")
            return

        self.btn_generate.setEnabled(False)
        self.btn_generate.setText("  Genererar...")
        self.log.append(f"Genererar ordlista om \"{topic}\"...")

        self.gen_worker = WordGeneratorWorker(topic, self.gen_count.value(), ai)
        self.gen_worker.words_ready.connect(self._on_words_ready)
        self.gen_worker.log.connect(lambda msg: self.log.append(msg))
        self.gen_worker.start()

    def _on_words_ready(self, words):
        self.btn_generate.setEnabled(True)
        self.btn_generate.setText("  Generera ordlista")
        if words:
            existing = self.word_input.toPlainText().strip()
            new_text = "\n".join(words)
            self.word_input.setPlainText(f"{existing}\n{new_text}".strip() if existing else new_text)
            self.log.append(f"Lade till {len(words)} ord.")
        else:
            self.log.append("Inga ord genererades.")

    def start_creation(self):
        deck = self.deck_input.currentText().strip()
        note_model = self.model_combo.currentText()
        field_f = self.field_front_combo.currentText()
        field_b = self.field_back_combo.currentText()
        ai_model = self.btn_ai_model.currentText()

        if not deck:
            self.log.append("Ange ett deck-namn.")
            return
        if not note_model or note_model.startswith("("):
            self.log.append("Välj en korttyp.")
            return
        if field_f == field_b:
            self.log.append("Framsida och baksida kan inte vara samma fält.")
            return

        words = [w.strip() for w in self.word_input.toPlainText().strip().split("\n") if w.strip()]
        if not words:
            self.log.append("Skriv in ord först (ett per rad).")
            return

        self.log.clear()
        self.progress.setMaximum(len(words))
        self.progress.setValue(0)
        self._start_time = time.time()
        self.progress.setVisible(True)
        self.btn_start.setVisible(False)
        self.btn_stop.setVisible(True)

        self.worker = CreatorWorker(words, deck, note_model, note_model, field_f, field_b, ai_model)
        self.worker.progress.connect(self._on_progress)
        self.worker.card_done.connect(self._on_card)
        self.worker.log.connect(lambda msg: self.log.append(msg))
        self.worker.finished.connect(self._on_done)
        self.worker.start()

    def stop_creation(self):
        if self.worker:
            self.worker.cancel()

    def _on_progress(self, i, total, word):
        self.progress.setValue(i + 1)
        eta = format_eta(self._start_time, i + 1, total)
        self.progress_label.setText(f"{i+1}/{total}  —  {word}  —  {eta}")

    def _on_card(self, result):
        self.preview.set_card(result["word"], result["html"], "Nytt kort")

    def _on_done(self, stats):
        self.btn_start.setVisible(True)
        self.btn_stop.setVisible(False)
        self.progress.setVisible(False)
        self.progress_label.setText(
            f"Klart!  Skapade: {stats['created']}  |  "
            f"Duplikater: {stats['skipped']}  |  Fel: {stats['error']}"
        )


# ─────────────────────────────────────────────────────────────
# MAIN WINDOW
# ─────────────────────────────────────────────────────────────

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anki-Svenska")
        icon_path = Path(__file__).parent / "anki_svenska.ico"
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))
        self.setMinimumSize(1100, 700)
        self.resize(1280, 800)

        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Sidebar ──
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet(f"""
            QFrame {{
                background: {COLORS['surface']};
                border-right: 1px solid {COLORS['border']};
            }}
        """)
        sb_lay = QVBoxLayout(sidebar)
        sb_lay.setContentsMargins(10, 16, 10, 16)
        sb_lay.setSpacing(4)

        # Logo
        logo = QLabel("Anki-Svenska")
        logo.setFont(QFont("Segoe UI", 16, QFont.Bold))
        logo.setStyleSheet(f"color: {COLORS['accent']}; background: transparent; padding-bottom: 6px;")
        sb_lay.addWidget(logo)

        version_label = QLabel("v2.0  —  Lokal AI")
        version_label.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 10px; background: transparent;")
        sb_lay.addWidget(version_label)

        sb_lay.addSpacing(20)

        # Deck selector
        deck_lbl = QLabel("DECK")
        deck_lbl.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 10px; font-weight: bold; letter-spacing: 2px; background: transparent;")
        sb_lay.addWidget(deck_lbl)
        self.deck_combo = QComboBox()
        self.deck_combo.setFixedHeight(34)
        self.deck_combo.currentTextChanged.connect(self._on_deck_change)
        sb_lay.addWidget(self.deck_combo)

        sb_lay.addSpacing(20)

        # Nav buttons
        nav_label = QLabel("NAVIGATION")
        nav_label.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 10px; font-weight: bold; letter-spacing: 2px; background: transparent;")
        sb_lay.addWidget(nav_label)
        sb_lay.addSpacing(4)

        self.nav_btns = []
        for icon, text, idx in [
            ("📊", "  Hem", 0),
            ("🔍", "  Skanna", 1),
            ("✨", "  AI-uppdatering", 2),
            ("📂", "  Kortläsare", 3),
            ("➕", "  Skapa deck", 4),
            ("⚙️", "  Inställningar", 5),
        ]:
            btn = QPushButton(f"{icon}  {text}")
            btn.setObjectName("nav")
            btn.setCheckable(True)
            btn.setFixedHeight(40)
            btn.clicked.connect(lambda checked, i=idx: self.navigate(i))
            sb_lay.addWidget(btn)
            self.nav_btns.append(btn)

        sb_lay.addStretch()

        # Connection indicators
        self.anki_dot = QLabel("● Anki")
        self.anki_dot.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 11px; background: transparent;")
        sb_lay.addWidget(self.anki_dot)
        self.ollama_dot = QLabel("● Ollama")
        self.ollama_dot.setStyleSheet(f"color: {COLORS['subtext']}; font-size: 11px; background: transparent;")
        sb_lay.addWidget(self.ollama_dot)

        root.addWidget(sidebar)

        # ── Main content ──
        content = QWidget()
        content_lay = QVBoxLayout(content)
        content_lay.setContentsMargins(28, 24, 28, 24)

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage(self)
        self.scanner = ScannerPage(self)
        self.updater_page = UpdaterPage(self)
        self.browser = BrowserPage(self)
        self.creator = CreatorPage(self)
        self.settings = SettingsPage(self)

        self.stack.addWidget(self.dashboard)      # 0
        self.stack.addWidget(self.scanner)         # 1
        self.stack.addWidget(self.updater_page)    # 2
        self.stack.addWidget(self.browser)         # 3
        self.stack.addWidget(self.creator)         # 4
        self.stack.addWidget(self.settings)        # 5

        content_lay.addWidget(self.stack)
        root.addWidget(content)

        # ── Keyboard shortcuts ──
        for i in range(6):
            QShortcut(QKeySequence(f"Ctrl+{i+1}"), self).activated.connect(
                lambda idx=i: self.navigate(idx))
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(
            lambda: self.dashboard.refresh_stats(self.current_deck()))
        QShortcut(QKeySequence("F5"), self).activated.connect(
            lambda: self.dashboard.refresh_stats(self.current_deck()))

        # ── Init ──
        self.navigate(0)
        QTimer.singleShot(200, self._init_connections)

    def navigate(self, index):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_btns):
            btn.setChecked(i == index)

    def current_deck(self) -> str:
        return self.deck_combo.currentText()

    def _on_deck_change(self, deck):
        if deck:
            QTimer.singleShot(100, lambda: self.dashboard.refresh_stats(deck))

    def _init_connections(self):
        """Kontrollera anslutningar — körs via QTimer efter att fönstret visats."""
        self._init_worker = InitWorker()
        self._init_worker.result.connect(self._on_init_result)
        self._init_worker.start()

    def _on_init_result(self, data):
        anki_ok = data["anki_ok"]
        decks = data["decks"]
        ollama_ok = data["ollama_ok"]
        models = data["models"]
        cache_count = data["cache_count"]

        # Anki
        if anki_ok:
            self.anki_dot.setStyleSheet(f"color: {COLORS['green']}; font-size: 11px; background: transparent;")
            self.anki_dot.setText("● Anki ansluten")
            if decks:
                self.deck_combo.blockSignals(True)
                self.deck_combo.addItems(sorted(decks))
                # Try to select McHP Anki
                for i in range(self.deck_combo.count()):
                    if "McHP" in self.deck_combo.itemText(i):
                        self.deck_combo.setCurrentIndex(i)
                        break
                self.deck_combo.blockSignals(False)
                # Trigger stats refresh for selected deck
                deck = self.current_deck()
                if deck:
                    self.dashboard.refresh_stats(deck)
        else:
            self.anki_dot.setStyleSheet(f"color: {COLORS['red']}; font-size: 11px; background: transparent;")
            self.anki_dot.setText("● Anki ej ansluten")

        # Ollama
        if ollama_ok:
            self.ollama_dot.setStyleSheet(f"color: {COLORS['green']}; font-size: 11px; background: transparent;")
            self.ollama_dot.setText(f"● Ollama ({len(models)} modeller)")
        else:
            self.ollama_dot.setStyleSheet(f"color: {COLORS['red']}; font-size: 11px; background: transparent;")
            self.ollama_dot.setText("● Ollama ej igång")

        # Populate model combos
        self.updater_page.refresh_models()
        self.creator.refresh_models()
        self.settings.refresh_models()
        self.settings.refresh_cache()
        self.settings.refresh_backups()

        # Dashboard status
        self.dashboard.update_status(anki_ok, ollama_ok,
                                     models[0] if models else "—", cache_count)


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(STYLESHEET)

    # Set dark palette as base
    palette = app.palette()
    palette.setColor(palette.ColorRole.Window, QColor(COLORS['bg']))
    palette.setColor(palette.ColorRole.WindowText, QColor(COLORS['text']))
    palette.setColor(palette.ColorRole.Base, QColor(COLORS['surface']))
    palette.setColor(palette.ColorRole.Text, QColor(COLORS['text']))
    palette.setColor(palette.ColorRole.Button, QColor(COLORS['card']))
    palette.setColor(palette.ColorRole.ButtonText, QColor(COLORS['text']))
    palette.setColor(palette.ColorRole.Highlight, QColor(COLORS['accent']))
    app.setPalette(palette)

    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
