# 共創待辦與里程碑

以下是原創起始規劃，**全部待認領／未開始**。沒有指定負責人、完成百分比或承諾日期。開始前查 [Issues](https://github.com/FreeTWAI-AI/freedom-skill-event-space/issues)／[PR](https://github.com/FreeTWAI-AI/freedom-skill-event-space/pulls)；把認領範圍與相依工作連回來，最新討論优先。

## M1：可複用的入門流程（planned）

完成條件：新增合成案例、模板欄位及其結構檢查；由維護者審查後才標完成。

### EVENT-01 · 補充雨天與場地異動的替代流程

- 狀態：proposed／未認領
- 範圍：在 templates/event-brief.md 加入切換時機、通知角色和替代地點欄位；提供一份全虛構範例。
- 驗收：雨天與室內取消各一例；不填真實場地或聯絡方式；現場分工可對回 run-of-show。
- 驗證：`python3 scripts/validate.py examples/event-plan.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

### EVENT-02 · 擴充讀書會主持流程

- 狀態：proposed／未認領
- 範圍：加入第一次參加者也能帶場的分組提問與收尾模板。
- 驗收：標示每段分鐘數；提供 6 人與 20 人兩個配置；保留安靜參與與不拍照選擇。
- 驗證：`python3 scripts/validate.py examples/event-plan.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

### EVENT-03 · 加入可存取性與動線檢查範例

- 狀態：proposed／未認領
- 範圍：用純文字或原創示意圖記錄入口、座位、設備及待場地方確認事項。
- 驗收：不把示意圖宣稱為消防核准；所有視覺有文字對照；附上實際檢查者應填的日期欄位。
- 驗證：`python3 scripts/validate.py examples/event-plan.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

## M2：由真實使用回饋改善（planned）

M1 後，由自願使用者提供可公開、已去識別的回饋。僅把實際收到的回饋列入 Issue；不預填活動成果、人數、成效或測試成功。跨公會協作可連結原 Issue，不重複複製責任。
