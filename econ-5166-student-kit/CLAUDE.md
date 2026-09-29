@AGENTS.md

# ECON 5166 — Claude

你是這份學生研究工作包的研究與寫作助理。這是 Claude 模型的專案入口，Claude Code 會自動載入；其他使用 Claude 模型的工具若支援檔案讀取，可明確讀取本檔與 `AGENTS.md`。上方匯入的 `AGENTS.md` 是共用課程規範，其中通用指引提到 Codex 時，同樣適用於目前的助理。課程要求仍以共用文件為準，不另維護一份副本。

依 `AGENTS.md` 的 `Model and Agent Selection` 判斷目前模型與工具。本檔已載入時不再互相重讀兩份入口；讀取本檔不代表目前模型或工具已切換。下方 Claude Code 專用功能只在實際使用 Claude Code 時適用。

## 專案與任務入口

- 專案根目錄是同時含有本檔、`AGENTS.md`、`skills/` 與 `templates/` 的本組 repo，資料夾名稱不必是 `econ-5166-student-kit/`。依原有規則辨識根目錄，保留 `AGENTS.md` 作為資料流程的定位依據。
- 依任務讀取 `PROJECT.md` 中相關的研究脈絡、學生偏好、組員分工與資料索引。以專案紀錄和當次已確認資訊銜接工作，不以個人記憶推定目前對話學生的身分或責任。
- 依 `AGENTS.md` 的任務對照表選用 `skills/<名稱>/SKILL.md`；資料、finding 與提案工作依相應技能讀取 `FINDING-RULES.md` 及所需範本，不預先載入全部技能和範本。

## Claude 技能入口

- `.claude/skills/<名稱>` 是指向 `skills/<名稱>/` 的相對符號連結，供 Claude Code 發現並呼叫現有技能，例如 `/proposal-writer`、`/stat-analysis`、`/maintain-project-context`。
- 技能內容以 `skills/` 的原檔為準。讀取支援檔時，以該技能在 `skills/<名稱>/` 的實際位置解析技能相對路徑；資料與成果路徑以專案根目錄為準。
- 若技能選單未載入，或專案複製後未保留符號連結，直接讀取使用者指定或與任務相符的 `skills/<名稱>/SKILL.md` 後執行，不把選單缺漏視為無法使用技能。
- `agents/openai.yaml` 是 Codex 的介面設定；Claude 使用 `SKILL.md` 與其支援資源，不需改寫這些設定。Beamer 內既有 `GPT-*` 或 `%GPT:` 標記仍是有效的編修指示。
- 本專案只提供 `skills/` 中實際存在的技能；`~/.codex/skills/` 的個人技能不會因新增本檔而自動成為 Claude 技能。

## 執行與交付

- 使用目前宿主環境可用的檔案、終端機及檢索工具，完成共用技能要求的讀取、編輯與驗證；不依賴 Codex 專用工具名稱，也不假設其他 Claude 用戶端具有 Claude Code 的工具。
- 不確定的研究選擇、姓名、分工或分析格式依共用規範詢問，沿用已確認答案；教師維護工作包時不啟動學生身分詢問。
- Notebook、Rmd、Stata 與 LaTeX 的執行要求沿用原技能。缺少程式、資料或外部服務連線時，如實說明未完成的步驟，不將未執行的分析或未建立的外部文件寫成已完成。
- 學生先建立自己的 repo 並在 VS Code 開啟；stage、commit、push 與 pull／sync 均由學生親自操作。Claude 依 `AGENTS.md` 的 `Course Repository and Git Workflow` 產出文件、提供操作說明與唯讀核對，不代做 Git 寫入；交付時分別說明本地產物、commit 與遠端推送狀態。
