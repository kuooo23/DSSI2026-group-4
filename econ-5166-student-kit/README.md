# ECON 5166 學生研究工作包

把資料、提案與分析範本、AI 研究助理放在同一個專案。學生提出構想、資料與想回答的問題，AI 透過討論協助釐清，再把已確認的內容整理成課程文件；提案由學生逐步作出研究選擇。**報告預設使用繁體中文（台灣用語，zh-TW）**，學生已指定其他語言時優先沿用。分析工具未指定時會詢問；提案沿用 Markdown。

## 開始使用

### 先建立本組的 GitHub repo

**學生先自行建立 repo，再在 VS Code 操作 commit 與 push。** AI 協助產出、檢查及整理貢獻紀錄，課程提交操作由學生完成。

1. 準備好 GitHub 帳號、Git 與 VS Code。學生在 GitHub 選 **New repository**，確認 Owner、名稱，按教師要求選擇公開／私人設定後建立本組 repo。使用全新的空 repo，不先加入 README、`.gitignore` 或 license，稍後由工作包帶入。小組共用 repo 時，由建立者設定組員需要的存取權限。[GitHub 建立 repo 說明](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
2. 在 VS Code 開啟命令選擇區（macOS：`Cmd+Shift+P`；Windows：`Ctrl+Shift+P`），執行 **Git: Clone**，貼上剛建立的 repo URL，選擇本機存放位置，再按 **Open**。已 clone 過時直接開啟該資料夾。[VS Code clone 說明](https://code.visualstudio.com/docs/sourcecontrol/quickstart#_option-a-clone-a-repository-locally)
3. 將教師工作包 `econ-5166-student-kit/` **裡面的完整內容**複製到 clone 出來的資料夾根目錄，包含 `.gitignore`、`.claude/` 等隱藏項目；`.claude/` 是 Claude 的技能入口，與共用規範都要保留。根目錄應直接看得到 `AGENTS.md`、`CLAUDE.md`、`PROJECT.md`、`skills/` 與 `templates/`，不要再多包一層 `econ-5166-student-kit/`。保留 clone 產生的 `.git/`，不要複製或覆蓋任何來源 repo 的 `.git/`。
4. 在 VS Code **Source Control（原始檔控制）**確認選到本組 repo 與預定分支，核對遠端 `origin` 指向剛建立的 GitHub repo。依下一節操作，完成工作包的第一次 commit 與 push。若出現 **Publish Branch**，確認它要發佈到既有的本組 `origin`；不要另外建立第二個 repo。

資料夾名稱可以是本組的 repo 名稱。以下所有 `data/`、`skills/` 等路徑，都相對於這個根目錄。每位組員使用自己的 Git 身分與 GitHub 登入，在自己的電腦 clone 同一個小組 repo；姓名與實際分工仍由學生提供。

建立後在 `PROJECT.md` 的 **Repository Context** 記錄已確認的 repo URL、`origin`、工作／提交分支與設定狀態；最近 push 的核對結果按實際證據更新。空白範本不代表已有 repo 或已完成 push。

### 在本組 repo 開始研究

1. 在使用中的 AI 工具開啟 **本組 repo 根目錄**（看得到 `AGENTS.md`、`CLAUDE.md`、`skills/` 與 `templates/` 的那一層）。AI 依已知的模型與工具選擇 Agent 入口；無法確認時才詢問，方式見下方說明。
2. **每組預設 3–4 位學生**，以本組已確認的實際名單為準。提供全組成員姓名、各自已確認的實際工作，並說明目前對話的你是哪位。AI 先沿用對話或 `PROJECT.md` 中已確認的資訊，只主動補問缺少的部分；分工未定時保留「待確認」，不自行填入作者或分工。
3. 把原始資料放進 `data/raw/`，或在對話中提供可讀取的檔案與來源說明。已整理資料可放 `data/processed/`，AI 仍會檢查資料結構與文件。
4. 先用自己的話說明關心的現象或初步疑問，以及為什麼想研究；不必一開始就有成熟、正式的研究題目。再參照下面的指令提出任務。作者、資料意義與其他關鍵資訊不明時，AI 會詢問。
5. 工具格式未指定時，回答 Python／Jupyter 或 R／R Markdown；AI 會記在本組 `PROJECT.md`。報告預設繁體中文與台灣用語，想用其他語言時可直接指定。
6. 直接檢閱選定的 **`.ipynb` 或 `.Rmd`**，確認程式、已核對的發現與實際執行狀態。教師直接驗收這份文件，不要求 HTML；只有另外提出匯出要求時才產生 HTML。

工作包目前包含 16 個技能，集中在 `skills/`，範本集中在 `templates/`。`AGENTS.md` 會依任務指引 AI 讀取相應的 `skills/<名稱>/SKILL.md`；Claude Code 由 `CLAUDE.md` 匯入同一份規範。你也可以直接指定技能檔案；技能清單是否出現在介面中，不影響依檔案指令使用這份工作包。

**學生先有自己的想法，AI 才開始研究討論。** AI 可根據你的觀察、疑問與研究動機，協助釐清問題、縮小範圍、檢查資料可行性、討論方法及改進題目表述。若只提供資料或說「幫我想題目」，AI 會先請你說明自己的觀察或疑問及想研究的原因；在收到想法前，不列研究題目清單、不替你選 outcome，也不撰寫實質 proposal。下面的指令與教師範本只是示例，請換成本組的想法。

**撰寫 proposal 的預設是分階段討論。** 每輪先由學生說明想法與理由，AI 簡短回饋並聚焦 1–2 個關鍵問題，學生再釐清或作出選擇。AI 將已確認的內容整理成相應段落，等主要研究選擇有依據後，再整合為六章節提案。AI 不一次丟出完整問卷，也不先代寫全篇、只請學生說「好」。已有答案會直接沿用，不為了湊對話輪數重問；讀取資料、核對檔案或修改已確認段落的文字可直接進行。

Demo 或代做以該次明確授權的範圍為限。例如「示範分工」只授權示範分工，不代表可以代選研究設計或完成整份提案；若明確要求完整 Demo，假設與示範內容會標示清楚，後續一般學生使用仍回到討論流程。

研究定義、資料處理方式、模型設定或作者等資訊不確定時，AI 會先與你討論，再進行依賴該設定的工作。**姓名與負責工作由學生提供，角色分工由學生決定**；AI 在學生開始使用時主動確認全組名單、各自已確認的實際工作及目前對話者，只問未知資訊，不自行指派 PM／DE／DA 或其他職責。3–4 位學生是預設值，已確認的人數不同時依實際名單記錄，不為符合預設補造或刪除成員；`PROJECT.md` 的 `Team` 表按確認名單一人一列。

AI 不從 Git 作者、電腦帳號、檔名、範本示例或「誰提供檔案」猜測作者與責任，不把目前對話的學生自動列為既有文件作者，也不為這項確認額外要求學號或 GitHub 帳號。缺少資訊時會先問，不只是留下空白；等待回答或依要求先做草稿時，未確認欄位保留「待學生填寫／待補」，可繼續不依賴歸屬的資料檢查或討論。已確認的選擇與繁體中文預設會沿用。

授課用簡報原始檔：[student-kit-slides.qmd](student-kit-slides.qmd)，可在 RStudio 預覽。

**上課原則：所有 contribution 都必須記錄成 commit。** 程式、資料處理、文件、提案與專案紀錄的修改都要保留提交紀錄，並隨成果更新 `PROJECT.md` 的 `Key Contributions` 表：**誰、做了什麼、commit reference**。外部成果須有已 commit 的說明或連結紀錄。尚未 commit 標示「待提交」，reference 尚未核對標示「待核對」；兩者都不算完成貢獻紀錄，檔案連結不能取代 commit。commit 次數不作為貢獻評分。

## 學生在 VS Code 手動 commit 與 push

AI 完成任務後，會列出修改檔案、驗證結果、建議 commit 訊息與目前提交狀態。**學生親自檢閱、stage、commit、push；AI 不代按按鈕，也不執行這些 Git 寫入操作。**

1. **檢閱變更**：儲存檔案，開啟 Source Control，確認 repo 與分支。點選 **Changes** 中的檔案查看 diff，確認程式、結果、作者及文字說明，也查看 Notebook 的實際輸出。
2. **選取本次成果**：逐一按檔案旁的 **+（Stage Changes）**，檢查 **Staged Changes** 是否只含這次要提交的成果與必要支援檔。不加入憑證、個資、無權上傳的資料、暫存檔或無關修改；資料無法上傳時，提交來源、取得方式及可重現的處理說明。
3. **Commit 到本機**：輸入說明這次成果的訊息，例如「完成讀書時數資料清理與驗證」，再按 **Commit**。這一步保存本機版本，尚未代表 GitHub 已收到。
4. **Push 到 GitHub**：在 Source Control 的 **…** 選單選 **Push**，將 commit 推到已設定的本組遠端分支。首次若顯示 **Publish Branch**，確認 repo／分支後由學生操作。**Sync Changes** 會先 pull 再 push；若有衝突或推送遭拒，先處理並檢閱變更，再重試，不用 force push 略過問題。
5. **核對遠端成果**：到本組 GitHub repo 的正確分支，開啟這次 commit，確認 SHA 與修改內容相符，檔案及必要支援檔都已上傳。看到本機 SHA 或 Source Control 沒有未提交變更，都不能單獨證明 push 已完成。

以上按鈕流程依 [VS Code 官方操作說明](https://code.visualstudio.com/docs/sourcecontrol/quickstart)。小組開始新一輪工作前，先由學生確認本機狀態，再 pull 組員的更新；有未提交變更時先妥善處理，避免覆蓋彼此成果。

### 回填貢獻紀錄與提交狀態

學生完成提交後，提供 commit 連結或 SHA；AI 可唯讀查看相應 commit 的 diff，核對它確實包含所描述的成果，再回填 `PROJECT.md` 的 `Key Contributions`。無法讀取或核對的 reference 標示「待核對」，不填入臆測或無關的 SHA。

| 可確認的狀態 | 紀錄方式 |
| --- | --- |
| 成果尚未 commit | `待提交（由學生在 VS Code 操作）` |
| reference 尚未核對內容 | `待核對`，保留學生提供的連結／SHA |
| 本機 commit 內容已核對，尚未 push | 真實 SHA，註明 `已 commit／待 push` |
| commit 已核對，遠端狀態尚無足夠證據 | 真實 SHA，註明 `已 commit／遠端待核對` |
| 已在指定 GitHub repo／分支核對同一 commit | 真實連結／SHA，註明 `已 push（遠端已核對）` |

學生自述已 push、僅提供 GitHub 形式的網址，或本機留有舊的遠端分支紀錄時，AI 會說明證據來源，未親自核對遠端就保留「遠端待核對」。沒有遠端讀取權限時，也可先完成本機內容核對。

**回填索引採下一次提交，不追逐同一份文件自己的 SHA。** 例如成果 commit 為 A，核對後將 A 填入 `PROJECT.md`，再由學生將這次索引更新 commit 為 B 並 push。A 繼續指向原成果，不改成 B；B 已記錄索引維護本身，不必再新增一列只為引用 B 而產生下一個 commit。具有獨立實質內容的專案脈絡更新仍須記錄成貢獻。每次交付都分別說明成果與尚未提交的索引狀態。

## 依使用模型選擇 Agent

學生不需要自行判斷要讀哪份規範。AI 會依目前環境可靠提供的資訊，或學生明確說明的模型與工具，按照 [入口選擇規則](AGENTS.md#model-and-agent-selection) 處理：

| 學生正在使用的模型／工具 | 選用入口 | 載入方式 |
| --- | --- | --- |
| Claude 家族（Opus、Sonnet、Haiku） | [CLAUDE.md](CLAUDE.md) | Claude Code 原生載入；其他工具需明確讀取本檔及共用規範 |
| OpenAI／GPT 家族 | [AGENTS.md](AGENTS.md) | Codex 原生載入；其他工具需明確讀取 |
| 其他已確認模型 | [AGENTS.md](AGENTS.md) 共用規範 | 目前沒有專用版本，使用工具實際支援的功能 |
| 模型與工具都不明 | 先詢問目前工具與模型 | 不猜測、不沿用別人的選擇 |

模型家族已知時依家族選入口，不必追問完整版本；只有模型家族也不明時，才依已確認的 Claude Code 或 Codex 工具選用入口。模型名稱不代表工具一定會讀取本機文件；若使用中的介面無法存取專案，需提供相應規範與技能檔案內容。選用 Agent 指的是讀取哪份工作指引，不會自行切換模型或開啟另一個服務。[Codex 官方載入方式](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[Claude Code 官方載入方式](https://code.claude.com/docs/en/memory#agentsmd)

AI 會將每位學生已確認的工具、模型與入口記錄在 [PROJECT.md 的 AI Agent Context](PROJECT.md#ai-agent-context)，同組可使用不同模型。已確認且仍適用的設定會沿用；更換工具或模型時更新該位學生的紀錄，教師修改工作包時不會代填學生設定。

## 使用 Claude Code

已安裝並登入 Claude Code 後，在終端機切換到這份學生工作包，再啟動：

```bash
cd /你的路徑/本組repo
claude
```

[CLAUDE.md](CLAUDE.md) 會匯入 [AGENTS.md](AGENTS.md)，讓 Claude Code 與 Codex 共用課程規範；未來調整課程要求時仍更新原有共用文件。可在 Claude Code 輸入 `/context` 查看載入的記憶檔案。此入口適用於 Claude Code。[官方載入與匯入說明](https://code.claude.com/docs/en/memory#agentsmd)

`.claude/skills/` 已為目前 16 個技能建立相對符號連結，指向 `skills/` 原檔。Claude Code 可使用 `/proposal-writer`、`/stat-analysis` 等技能指令；修改技能時只需編輯 `skills/`。新增或刪除技能時，也同步增刪對應的 Claude 連結。[官方技能目錄說明](https://code.claude.com/docs/en/skills#choose-where-skills-load)

也可以直接貼上以下指令，或沿用本 README 其他指定技能檔案的範例：

```text
請讀取 skills/proposal-writer/SKILL.md，依課程規範帶我們分階段討論提案。
先沿用 PROJECT.md 中已確認的資料，再詢問尚缺少的姓名、分工與初步研究想法。
```

若 Windows 或解壓縮工具未保留符號連結，仍可用上述指定 `skills/<名稱>/SKILL.md` 的方式。`AGENTS.md`、`FINDING-RULES.md`、`PROJECT.md`、`skills/` 與 `templates/` 都需一起保留。Claude Code 仍使用本機可用的 Python、R、Stata 或 LaTeX；程式與外部服務連線依實際任務準備。

## 可以直接說

> 我是王小明，這次負責資料整理與統計分析。我把資料放在 data/raw/。請先看資料與課程規範，詢問我想用的工具格式，再幫我整理資料，分析教育年數與薪資的關聯。

也可以指定技能：

```text
請讀取 skills/stat-analysis/SKILL.md，
用 data/processed/wages.csv 製作統計分析 finding。
研究問題：教育年數與薪資的關聯。我是王小明，這次負責統計分析與結果說明。
```

如果你已經決定偏好，可以一次說清楚：

```text
請讀取 skills/prediction-model/SKILL.md。
請用 Python／Jupyter Notebook、繁體中文，
以 data/processed/train.csv 與 test.csv 預測 sales。
我是王小明，這次負責預測模型與績效評估。
請依課程範本分別報告訓練與測試績效，交付保留執行輸出的 Notebook。
```

分析未提供工具偏好時，AI 會先問「Python／Jupyter Notebook 或 R／R Markdown？」。報告語言未指定時直接使用繁體中文與台灣常見措辭，不再另外詢問；範本原有英文欄名保留。提案與純連結索引沿用 Markdown，不必為寫作選擇 R／Python；明確選用 Stata 時按教師的 Stata 專用格式處理。已指定的選擇不重複詢問。

要寫研究提案，先提供全組成員姓名、各自已確認的實際工作及目前對話者；已確認的資訊不必重複提供。每組預設 3–4 位學生，以實際名單為準。再提供本組自己的初步想法、研究動機與已有資料。尚未分配的工作由組員決定，AI 會先詢問並保留「待確認」。討論可按「問題與動機 → 資料範圍與變數 → 方法與假說 → 限制」逐步進行，依已有答案跳過已釐清內容；各階段整理已確認的段落，最後連同資料說明與實際分工整合為範本六節：

```text
請讀取 skills/proposal-writer/SKILL.md，帶我們分階段討論並完成繁體中文 proposal。
我是王小明，這次負責整理本組提案；其他成員的姓名與已確認工作列在附上的分工筆記。
初步想法：我們觀察到住在公車較少地區的同學，找打工的範圍可能較受限。
想研究的原因：我們想了解交通條件是否與就業機會有關。
請從我們已有的想法開始，每輪先簡短回饋，再問 1–2 個關鍵問題，讓我們說明理由或作出選擇。
先討論問題與動機，再逐步釐清資料範圍、變數、方法、假說與限制；已有答案的部分不必重問。
每階段把已確認內容整理成段落，最後才依範本整合六節提案。
這是我們的討論筆記、組員分工與已取得的資料樣本。
尚未確定的資料或設計請標示待補並討論，不要替我們定案；產出放在 report/。
```

例如，若本組已提出「公館地下道填平後的交通事故效益」，AI 可先問「你們觀察到什麼變化，才想研究這個問題？」與「你們說的效益，最想了解哪種事故變化？為什麼？」。收到回答後，再根據學生的定義檢視已有資料，討論研究範圍與可行方法；不只因為已有題目就直接交付全篇草稿。

要先完成資料流程，再接續分析，可以這樣說：

```text
請用 data-preparation，依範本整理我放在 data/raw/ 的資料。
使用 R Markdown、繁體中文；請完成原始資料說明、處理程式與整理後資料說明，
將實際輸出與檢查結果記錄在 PROJECT.md，讓後續分析可以接著使用。
```

也可以只指定 `raw-data-documentation`、`data-processing` 或
`processed-data-documentation` 完成其中一階段。已有合適整理檔時可直接建立說明與驗證，不必重做全部流程。

要維護已有文件或專案紀錄，可以這樣說：

```text
請用 maintain-data-documentation，更新 data/raw/ 與 data/processed/ 的既有說明文件。
沿用各文件的格式，核對本次更新的資料、變數定義、來源、摘要與連結，
同步 PROJECT.md 的 Data Artifacts，並指出仍使用舊資料版本的文件或 finding。
```

```text
請用 maintain-project-context，依本次已確認的討論與實際成果更新 PROJECT.md。
維持 Data and Current Focus 表格，並在 Key Contributions 記錄
誰、做了什麼、對應的 commit 連結或 SHA；未 commit 標示待提交，不能視為完成貢獻紀錄。
```

資料文件維護會沿用既有 `.ipynb`／`.Rmd`，依變動範圍核對實際結果；
單純修改說明不會自動重做資料處理或重跑 finding。只維護 `PROJECT.md`
不必另選 R／Python，也不需要另外填寫週報。

## 產出會議記錄

`meeting-minutes` 可將會議筆記、逐字稿或條列重點整理成繁體中文 `.md` 會議記錄，也可產生空白範本。**目前此 skill 安裝於本機的 `~/.codex/skills/meeting-minutes/`，尚未包含在學生工作包內**；在其他電腦使用前，需另外安裝完整的 `meeting-minutes` 資料夾（包含 `SKILL.md`、`agents/` 與 `assets/`）。

此處的 `$meeting-minutes` 是 Codex 的使用範例；本次 Claude Code 入口未另外安裝這個個人技能。在 Codex 已安裝後，可以直接說：

```text
請使用 $meeting-minutes，將以下會議筆記整理成繁體中文 .md 會議記錄，
存放在本專案的 report/ 資料夾：
（貼上會議筆記或逐字稿）
```

格式依照教師提供的 [會議記錄範本](https://docs.google.com/document/d/1OuQQldAU34VLieXM32yKS1zEBpJmrDuEoj7Xr1HIpEI/edit?tab=t.xetwuewysfie)，保留原標題及括號內說明，依序為：

1. 會議目標 / 議程
2. Key Takeaway
3. 共識與決策
4. 後續行動（會議後開 Issue）
5. 未解決問題
6. 其他

未指定議程時沿用「驗收進度、釐清並解決目前的阻礙、討論後續行動與分工」三項。尚未定案的提議會保留待確認狀態；缺少的負責人與期限不會自行補造。格式已保存於 skill 的 `assets/meeting-minutes-template.md`，日常使用不必重新讀取 Google 文件。

未指定輸出位置時，檔案放在目前工作目錄；有確定會議日期時命名為 `YYYY-MM-DD-會議記錄.md`，否則使用 `會議記錄.md`。同名新記錄會加上序號。若只要空白範本，可說「請使用 $meeting-minutes，在 report/ 產生空白會議記錄範本」。

此技能負責整理並寫出會議記錄；範本中的「會議後開 Issue」是提醒，產出檔案不代表已建立 Issue。小組也可自行填寫工作包內的 [週報範本](templates/weekly-meeting.md)，記錄進度與會議決定。

## 課程技能

| 任務 | Skill | 主要輸出 |
| --- | --- | --- |
| 與學生分階段討論研究選擇、整理已確認段落與提案撰寫／修改 | `proposal-writer` | `report/` 六章節 Markdown proposal |
| 串接原始說明、處理與整理後說明 | `data-preparation` | 依任務協調下列三個技能 |
| 原始資料來源、變數、樣本與摘要 | `raw-data-documentation` | `data/raw/` 說明 `.ipynb`／`.Rmd`，原檔保留 |
| 資料清理、合併、轉形與切分 | `data-processing` | `data/code/` 處理 `.ipynb`／`.Rmd`，資料寫入 `data/processed/` |
| 整理後資料說明、斷言與分析銜接 | `processed-data-documentation` | `data/processed/` 說明 `.ipynb`／`.Rmd`，核對實際檔案 |
| 維護已有 raw／processed 資料說明 | `maintain-data-documentation` | 更新既有文件、版本與檢查紀錄，同步資料索引 |
| 維護專案脈絡、目前焦點與貢獻紀錄 | `maintain-project-context` | 更新 `PROJECT.md`，貢獻表列出姓名、成果與 commit reference |
| 敘述統計、圖表、檢定、迴歸 | `stat-analysis` | `finding/` 統計分析，選定的 `.ipynb` 或 `.Rmd` |
| 預測與 train/test 模型評估 | `prediction-model` | `finding/` 預測模型，選定的 `.ipynb` 或 `.Rmd` |
| 數值模擬 | `simulation-runner` | `finding/` 模擬 Notebook／Rmd，沿用原範本 |
| Stata 工作與紀錄 | `stata-analysis` | 同名 `.md`、`.do` 與 Google Doc；純連結登記維持 `.md` |
| 外部文件、簡報或成果連結 | `external-file` | `finding/` 或 `report/` Markdown 索引 |
| 搜尋與比較研究文獻 | `paper-search` | 文獻清單、分類與比較 |
| 整理論文閱讀筆記 | `paper-note` | `references/` Markdown 筆記 |
| 建立研究成果簡報 | `beamer-slides` | `deliverable/slides/` Beamer 簡報 |
| 修改既有研究簡報 | `revise-beamer-slides` | 依註解修訂既有 Beamer 簡報 |

統計與預測依 `templates/finding/` 範例及教師的現行規則撰寫：Python 使用 `.ipynb`，R 使用 `.Rmd`。教師最新指示已取代[原文](https://docs.google.com/document/d/1sl6gEFMdmiGsiNjLe17UmZ30xKxq15U0Mb2B-Jvusxg/edit?tab=t.33iie8ybx7s4)的同名 HTML 要求，直接驗收選定的分析文件，不預設匯出 HTML。Stata 的 Google Doc 仍將 `.do` 程式與對應結果逐段排列，另交同名 `.md` 與 `.do`。模擬沿用原 `.Rmd`／`.ipynb` 範本。

檔名沿用學生指定、既有名稱或清楚的內容描述，例如 `rct_engagement.Rmd` 或 `rct_engagement.ipynb`；教師已取消來源中的會議日期命名要求。純外部索引用外部檔案的同一 basename 加 `.md`。

統計與預測都需在正式分析前提供所有使用變數的敘述統計。圖表須有清楚標籤、樣本與文字說明；估計量圖附 95% 信賴區間。迴歸須交代 outcome 平均、穩健／群聚標準誤、參考組及固定效果。預測的指定指標與圖表見 [共用規則](FINDING-RULES.md)。

省略 HTML 不代表省略執行。Jupyter 會從乾淨 kernel 順序執行，並把輸出保留在 `.ipynb`。Rmd 可在乾淨 R 程序中用 `knitr::knit()` 將結果寫到暫存位置，檢查數字與圖表後，把已確認的發現寫回 `.Rmd`；不需繳交暫存驗證產物。只有你另外要求時，AI 才匯出 HTML，並核對它與分析文件一致。

程式與文件能否完成取決於環境與資料；未執行或部分執行時，文件會說明具體狀態，不宣稱完整分析已完成。統計／預測由學生提交到 GitHub 的成果為選定的 `.ipynb` 或 `.Rmd`；Stata 仍提交 `.md` 與 `.do`。AI 交付可檢閱內容並說明狀態，學生依上方流程自行 commit 與 push。建立外部文件仍須有相應授權，與 Git 提交流程分開處理。

## 資料夾

```text
本組repo/                      複製學生工作包內容後的根目錄
├── AGENTS.md                  專案共同規範與技能入口
├── CLAUDE.md                  Claude Code 入口，匯入共用規範
├── .claude/skills/            Claude 技能入口，連結至 skills/ 原檔
├── README.md                  學生使用說明
├── PROJECT.md                 研究問題、學生偏好與資料索引
├── FINDING-RULES.md            資料與 finding 的共用操作規則
├── skills/                    所有課程與研究 skills
│   ├── proposal-writer/
│   ├── data-preparation/
│   ├── raw-data-documentation/
│   ├── data-processing/
│   ├── processed-data-documentation/
│   ├── maintain-data-documentation/
│   ├── maintain-project-context/
│   ├── stat-analysis/
│   ├── prediction-model/
│   ├── simulation-runner/
│   ├── stata-analysis/
│   ├── external-file/
│   ├── paper-search/
│   ├── paper-note/
│   ├── beamer-slides/
│   └── revise-beamer-slides/
├── templates/                 所有可套用的範本
│   ├── data/
│   │   ├── raw/              原始資料說明範本（ipynb／Rmd）
│   │   ├── code/             處理程式範本（ipynb／Rmd）
│   │   └── processed/        整理後資料說明範本（ipynb／Rmd）
│   ├── finding/               統計、預測、模擬及成果紀錄
│   ├── report/                提案與外部報告
│   └── weekly-meeting.md      週報範本
├── data/                      raw / code / processed / temp
├── finding/                   學生的分析成果
├── report/                    學生的報告與選用週報
├── references/                文獻與研究筆記
├── attachments/               筆記與週報圖片
└── deliverable/               paper / slides / app
```

大量清理放在 `data/code/`；統計與預測 finding 讀取 `data/processed/`。模擬可以自行生成資料。範本中的 `/data/...` 指的是本專案資料夾，並非電腦根目錄。

資料銜接順序是 **原始檔與說明 → 處理 Notebook／Rmd → 已驗證的整理檔與說明 → finding**。
`PROJECT.md` 的 `Data Artifacts` 連結每份資料的實際路徑、文件、產生程式及角色；AI 檢查磁碟上的檔案後記錄驗證結果與 SHA-256（用來辨識檔案內容版本）。後續分析依這份紀錄核對並讀取精確檔案，程式會在資料消失或版本改變時明確停止，避免誤讀其他檔。更新資料後，AI 會指出哪些既有分析仍使用舊資料；任務包含重分析時才重新產出結果。

三種資料文件皆沿用相應正式範本，由學生選擇 ipynb 或 Rmd；資料文件沒有另外新增必交 HTML。

## 沿用 yc-ai-assistant 的方式

`skills/` 只放技能及其支援資源；`templates/` 只放可供學生套用的範本。共用規則與流程放在根目錄。每個 skill 都是指引 AI 工作的 `SKILL.md`：按需讀取相關文件、確認輸入、選擇範本、產出成果、檢查證據。Markdown 保存研究脈絡；正式論文、簡報與程式各在對應位置。沒有另建自動任務執行器。

保留學生可用於文獻整理與成果報告的 `paper-note`、`paper-search`、`beamer-slides`、`revise-beamer-slides`。課程技能涵蓋提案、資料準備與文件維護、專案紀錄、統計、預測及外部成果；原有 `simulation-runner` 也已對齊課程範本。

`proposal-writer` 從學生自己提出的想法與動機出發，透過分階段討論與學生的研究選擇逐步整理段落，再使用 [提案範本](templates/report/econ-5516-proposal-template.md) 整合專案敘述、已有 raw data、分析資料需求、假說與預期結果、限制、角色分工六節。範例中的題目、人名、模型與圖片不會直接當作學生的內容；未取得的資料會明確標示。提案不另要求 Notebook 或 HTML。

小組若需要每週紀錄，可自行填寫 [週報範本](templates/weekly-meeting.md)，由成員更新進度，會後記錄已確認的決策與後續行動。需要整理會議筆記時，可使用另行安裝的 `meeting-minutes`，方式見上方「產出會議記錄」。

## 課程與範本來源

整合來源為 `fa-25-econ-5166-group-project-template-main` 與 `yc-ai-assistant-main`。本次只將教師貼出的資訊搜集、統計分析、Stata 與預測模型要求整理至 [finding 共用規則](FINDING-RULES.md)，並依後續指示取消固定的會議日期命名與必交 HTML。現行統計／預測成果直接以選定的 `.Rmd` 或 `.ipynb` 驗收；其他章節不新增為要求，模擬維持原範本。

原 README 的另一份 [課程交付規範](https://docs.google.com/document/d/17YY_T9vu77ssXM6swrmNqx23nYT6hnxEF7jRUkGqqV4/edit?usp=sharing) 仍保留供學生查閱，尚未核對其完整內容；不可與此次已讀取的 `/finding/` 分頁混為一談。

提案範本另由教師指定的 Google 文件轉為本地 Markdown，保留原文章節、表格與三張圖片。`proposal-writer` 直接讀取這份本地範本，不把 finding 的交付要求延伸到提案。

整合版修正 `Future Direciton` 拼字、prediction Notebook 的粗體標記、資料處理範本的 `data/final` 路徑、R 範本混入的 `df.head(10)` 與轉檔占位文字，並清除 iris 範例執行輸出。原 Background 欄位與順序保留；預測範本在讀取資料後補入教師規範要求的摘要統計，統計／預測範本另補圖表、績效與執行驗證說明。原先的配對 HTML 規則已由教師最新指示取代。

## 整合版驗證

2026-09-15 檢查目前學生包：16 個技能的結構與 16 個 Claude 相對連結有效，文件相對連結已核對；6 份 Notebook 通過格式檢查，36 個 Python 程式區塊通過語法解析。本次已統一 Codex／Claude、相關技能及教學文件的學生手動 Git 流程，並同步更新發放 ZIP。這些是結構、語法與指引檢查，未重新執行完整分析或渲染簡報；教師範本目前沒有 `.git`，也未替學生實際 commit／push。

以下保留過往版本的測試紀錄，其中技能數量與 HTML 產物均反映當時版本。現行工作包包含 16 個技能，HTML 不是目前的交付要求；這些歷史紀錄不代表已重新測試取消 HTML 或本次技能精簡後的所有流程。

當時版本的 21 個 skills 已通過結構驗證，6 份 Notebook 範本通過格式檢查，6 份 Rmd 範本程式區塊通過語法檢查，相關文件連結已核對。2026-09-11 以固定種子 51660911 的隔離人工資料，實測新增的 `data-preparation`、`stat-analysis`、`prediction-model`、`external-file` 與 `proposal-writer`：6 份 Python Notebook 共 43 個程式區塊執行成功，R 統計分析成功產出 Rmd 與同名 HTML；資料整理結果、HC1 迴歸及連續／二元預測指標均與獨立計算一致，分析 HTML 與圖表已檢視。外部紀錄的建立、更新歷史、逐字稿及提案六章節、資料引用也已核對；缺少偏好時先詢問且不產出檔案的情境通過。

新增三個資料技能後，再以種子 51660912 完整實跑 Python 與 R 資料流程：5 份 Jupyter Notebook（26 個程式區塊）及 3 份 Rmd 成功執行，存檔內容與獨立計算一致，原始資料保持不變。新的分析對話只從 `PROJECT.md` 接手，正確找到 87 筆統計資料及 93／31 筆 train/test，並產出 Rmd／ipynb 與同名 HTML；迴歸及預測指標與獨立計算一致。整個專案搬到含空格的新路徑後可重跑，資料缺失或內容版本改變時會停止，沒有誤用旁邊的不相關 CSV。測試中發現的資料欄名文字、processed Summary 標題及預測範本註解換行已修正。

上述歷史測試依教師指示排除 Stata，當時原有 skills（含 `simulation-runner`）未重測。測試涵蓋上述具體案例，不代表所有資料、模型與環境均已驗證。當時測試資料與成果另存於工作包外，未放進學生工作目錄。

2026-09-11 最新驗收已依直接檢閱 Rmd／ipynb 的指示，使用同一份人工資料測試 8 個新增技能（排除 Stata）：10 份已執行 ipynb、10 份以乾淨 R 程序 knit 驗證的 Rmd，以及 3 份 Markdown。已確認實際結果、支援圖檔、資料版本綁定及三種不確定資訊的詢問行為；測試產物另存於學生包外，沒有加入學生範本。
