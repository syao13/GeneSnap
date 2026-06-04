# Pagination for VariantTable

**Date:** 2026-06-03
**Status:** Approved

## Overview

Add client-side pagination to `VariantTable` showing 100 rows per page, with prev/next buttons and numbered page links. Reduces initial render cost for large variant lists.

## Components

### New: `src/components/Pagination.tsx`

A stateless display component.

**Props:**
- `page: number` — current page (1-based)
- `totalPages: number` — total number of pages
- `onPageChange: (page: number) => void`

**Rendering rules:**
- Prev button: disabled when `page === 1`
- Next button: disabled when `page === totalPages`
- Page numbers: always show page 1 and page `totalPages`; show a window of ±2 around current page; collapse gaps ≥ 2 with `…`
  - Example at page 5 of 12: `1 … 3 4 [5] 6 7 … 12`
  - Example at page 1 of 3: `[1] 2 3`
- Hidden entirely when `totalPages <= 1`

### Modified: `src/components/VariantTable.tsx`

- Add `PAGE_SIZE = 100` constant
- Add `page` state, default 1
- `useEffect` resets `page` to 1 when `matches` prop changes (tab switch)
- Slice `matches` before mapping rows: `matches.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)`
- Render `<Pagination>` below both the desktop table and mobile card list when `totalPages > 1`

## Behavior

- Page resets to 1 on tab switch
- Expand/collapse state (`expandedRsid`) resets implicitly on tab switch (existing behavior unchanged)
- Pagination bar is hidden when all items fit on one page

## Out of Scope

- Server-side pagination
- Per-tab page memory across tab switches
- URL-based page state
