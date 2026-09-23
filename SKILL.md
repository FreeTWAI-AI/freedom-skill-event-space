---
name: freedom-event-space
description: 把讀書會、聚會或小型展演整理成場地 brief、動線與現場分工。
---

# 活動與空間實作手冊

## 適用範圍

適用讀書會、社群聚會與小型活動的需求整理。模板不會替你訂場地、簽約、收款或認證現場安全。

## 輸入

- 活動目的、預計人數、日期範圍與可用預算
- 候選場地提供的設備、容量及使用條件
- 可投入的夥伴與主办人確認的聯絡方式（公開範例使用虛構資料）

## 執行步驟

1. 複製 templates/event-brief.md，填活動目的、人數、日期與場地需求。
2. 比較候選場地，記錄報價來源、進撤場時段、無障礙需求與場地方待確認項目。
3. 用 templates/run-of-show.csv 排出報到、開場、討論、收尾；每一段填負責角色。
4. 在 templates/event-plan.json 寫容量、人數與分工，再執行驗證。
5. 由主辦人核對未決事項；活動後記錄實際變更，刪除個資再提交模板改善 PR。

## 輸出與驗收

一份可交接的讀書會企劃：場地條件、流程、分工與備援。

```sh
python3 scripts/validate.py examples/event-plan.json
python3 -m unittest discover -s tests -v
```

驗證結果只描述結構檢查；實地確認、內容授權、參與者同意及實際成效必須另由當事人提供，未知保持未知。不要把模板範例當成已發生事實。

## 協作交接

1. 查 [BACKLOG.md](BACKLOG.md)、[Issues](https://github.com/FreeTWAI-AI/freedom-skill-event-space/issues) 與 [PR](https://github.com/FreeTWAI-AI/freedom-skill-event-space/pulls) 的最新狀態，避免重複工作。
2. 在已授權範圍內選一個待辦，用自己的 Fork／分支製作最小可審查變更。尚未派工時先在 Issue 協調；當前使用者已明確派工則直接沿用。
3. PR 目標 `https://github.com/FreeTWAI-AI/freedom-skill-event-space:main`。列 task id、變更用途、實跑命令、結果、未驗證項目及相依 PR。
4. 保留作者、來源與審查結果。Agent 可讀此技能，不因此取得帳號、發送訊息、付款、現場設備或平台資料的操作權。

## 邊界

- 本包不取代場地管理者的容量、逃生動線、器材或用電確認。
- 公開 repo 不放真實聯絡電話、名單、付款資料、場地門禁與簽約文件。
- 場地訂約、對外邀請及收費由當事人依既有授權操作；模板本身不授予這些權限。
