---
tags: [development, schedule]
date: 2025-08-29
---

# Development Schedule

A collaborative timeline for OASIS development. Update this page through pull requests and link to contributions as tasks are completed.

Since February 2025, OASIS has grown from an initial scaffold into a tagged documentation site. Late August 2025 added sidebar tag pages, fixed tag links, and launched the Cloud Triangle lesson with examples. Our next steps are to link tasks directly to GitHub issues and automate Gantt chart updates so the roadmap stays current.

## Historical Task List

- [x] [Initial repository setup](https://github.com/CU-ESIIL/home/commit/323aea0) — 2025-02-05
- [x] [Tag-based navigation](https://github.com/CU-ESIIL/home/pull/29) — 2025-08-13
- [x] [Static tag system](https://github.com/CU-ESIIL/home/pull/32) — 2025-08-14
- [x] [Repository structure docs](https://github.com/CU-ESIIL/home/pull/34) — 2025-08-14
- [x] [Development schedule page](https://github.com/CU-ESIIL/home/pull/35) — 2025-08-14

- [x] [Sidebar tag pages](https://github.com/CU-ESIIL/home/pull/55) — 2025-08-19
- [x] [Fix tag links in sidebar](https://github.com/CU-ESIIL/home/pull/56) — 2025-08-19
- [x] [Cloud Triangle scaffold](https://github.com/CU-ESIIL/home/pull/57) — 2025-08-22
- [x] [Cloud Triangle overview](https://github.com/CU-ESIIL/home/pull/58) — 2025-08-22
- [x] [Cloud Triangle examples & figure](https://github.com/CU-ESIIL/home/pull/59) — 2025-08-22

## Upcoming Task List

<!-- upcoming-start -->
- [ ] [Add GitHub linking to tasks](https://github.com/CU-ESIIL/home/issues/60)
- [ ] [Automate Gantt chart updates](https://github.com/CU-ESIIL/home/issues/61)
- [ ] [Interactive Cloud Triangle lesson](https://github.com/CU-ESIIL/home/issues/62)
<!-- upcoming-end -->


## Timeline Overview

| Task | Start | End | Contributors |
|------|-------|-----|--------------|
| Initial repository setup | 2025-02-05 | 2025-02-05 | [Ty Tuff](https://github.com/tytuff) |
| Tag-based navigation | 2025-08-13 | 2025-08-13 | [Ty Tuff](https://github.com/tytuff) |
| Static tag system | 2025-08-14 | 2025-08-14 | [Ty Tuff](https://github.com/tytuff) |
| Repository structure docs | 2025-08-14 | 2025-08-14 | [Ty Tuff](https://github.com/tytuff) |
| Development schedule page | 2025-08-14 | 2025-08-14 | [Ty Tuff](https://github.com/tytuff) |
| Sidebar tag pages | 2025-08-19 | 2025-08-19 | [Ty Tuff](https://github.com/tytuff) |
| Fix tag links in sidebar | 2025-08-19 | 2025-08-19 | [Ty Tuff](https://github.com/tytuff) |
| Cloud Triangle scaffold | 2025-08-22 | 2025-08-22 | [Ty Tuff](https://github.com/tytuff) |
| Cloud Triangle overview | 2025-08-22 | 2025-08-22 | [Ty Tuff](https://github.com/tytuff) |
| Cloud Triangle examples & figure | 2025-08-22 | 2025-08-22 | [Ty Tuff](https://github.com/tytuff) |
| Add GitHub linking to tasks | 2025-08-15 | 2025-08-21 | TBD |
| Automate Gantt chart updates | 2025-08-22 | 2025-08-26 | TBD |

## Gantt Chart

```mermaid
gantt
    title OASIS Development Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d
    section History
    Initial repository setup  :done, hist1, 2025-02-05, 1d
    Tag-based navigation      :done, hist2, 2025-08-13, 1d
    Static tag system         :done, hist3, 2025-08-14, 1d
    Repository structure docs :done, hist4, 2025-08-14, 1d
    Dev schedule page         :done, hist5, 2025-08-14, 1d
    Sidebar tag pages         :done, hist6, 2025-08-19, 1d
    Fix tag links             :done, hist7, 2025-08-19, 1d
    Cloud Triangle scaffold   :done, hist8, 2025-08-22, 1d
    Cloud Triangle overview   :done, hist9, 2025-08-22, 1d
    Cloud Triangle examples   :done, hist10, 2025-08-22, 1d
    section Planned
<!-- gantt-start -->
    Add GitHub linking to tasks  :active, plan1, 2025-08-15, 7d
    Automate Gantt chart updates  : plan2, 2025-08-22, 5d
    Interactive Cloud Triangle lesson  : plan3, 2025-08-29, 5d
<!-- gantt-end -->

```

<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 8px;
    border-bottom: 1px solid #ddd;
  }
  tr:hover {
    background-color: #f5f5f5;
  }
  .task-list li {
    background: #f5f5f5;
    border-radius: 8px;
    padding: 0.5rem;
    margin: 0.5rem 0;
    list-style: none;
  }
</style>
