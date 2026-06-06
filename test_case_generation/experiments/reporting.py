import csv
import json
from pathlib import Path
from datetime import datetime

def write_summary(results_dir: Path, log_func):
    rows = []
    for wsite in sorted(results_dir.iterdir()):
        if not wsite.is_dir() or wsite.name.startswith("."):
            continue
        for mdir in sorted(wsite.iterdir()):
            if not mdir.is_dir():
                continue
            for adir in sorted(mdir.iterdir()):
                if not adir.is_dir():
                    continue
                tc_file = adir / "test-cases.json"
                row = {
                    "website": wsite.name, "model": mdir.name,
                    "approach": adir.name, "status": "MISSING",
                    "total": 0, "positive": 0, "negative": 0, "edge": 0,
                    "high": 0, "medium": 0, "low": 0,
                }
                if tc_file.exists():
                    try:
                        data = json.loads(tc_file.read_text(encoding="utf-8"))
                        if "total_summary" in data:
                            s = data["total_summary"]
                            row.update({
                                "status":   "OK",
                                "total":    s.get("total_tests", s.get("total", 0)),
                                "positive": s.get("positive", 0),
                                "negative": s.get("negative", 0),
                                "edge":     s.get("edge", 0),
                                "high":     s.get("high_priority", 0),
                                "medium":   s.get("medium_priority", 0),
                                "low":      s.get("low_priority", 0),
                            })
                        elif "summary" in data:
                            s = data["summary"]
                            row.update({
                                "status":   "PARSE_ERR" if data.get("parse_error") else "OK",
                                "total":    s.get("total", 0),
                                "positive": s.get("positive", 0),
                                "negative": s.get("negative", 0),
                                "edge":     s.get("edge", 0),
                                "high":     s.get("high_priority", 0),
                                "medium":   s.get("medium_priority", 0),
                                "low":      s.get("low_priority", 0),
                            })
                        else:
                            row["status"] = "UNKNOWN_FORMAT"
                    except Exception as e:
                        row["status"] = f"ERR:{e}"
                rows.append(row)

    if not rows:
        log_func("No results found to summarise.")
        return

    fields = ["website", "model", "approach", "status",
              "total", "positive", "negative", "edge", "high", "medium", "low"]
    csv_path = results_dir / "experiment_summary.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    log_func(f"Summary CSV  -> {csv_path}")

    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Experiment Results Summary\n",
        f"Generated: {ts}\n",
        "| Website | Model | Approach | Status | Total | Positive | Negative | Edge | High | Medium | Low |",
        "|---------|-------|----------|--------|-------|----------|----------|------|------|--------|-----|",
    ]
    for r in rows:
        lines.append(
            f"| {r['website']} | {r['model']} | {r['approach']} | {r['status']} "
            f"| {r['total']} | {r['positive']} | {r['negative']} | {r['edge']} "
            f"| {r['high']} | {r['medium']} | {r['low']} |"
        )
    md_path = results_dir / "experiment_summary.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log_func(f"Summary MD   -> {md_path}")
