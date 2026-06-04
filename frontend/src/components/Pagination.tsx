interface PaginationProps {
  page: number
  totalPages: number
  onPageChange: (page: number) => void
}

function getPageItems(page: number, totalPages: number): (number | '...')[] {
  const toShow = new Set<number>([1, totalPages])
  for (let i = page - 2; i <= page + 2; i++) {
    if (i >= 1 && i <= totalPages) toShow.add(i)
  }
  const sorted = Array.from(toShow).sort((a, b) => a - b)
  const items: (number | '...')[] = []
  for (let i = 0; i < sorted.length; i++) {
    if (i > 0 && sorted[i] - sorted[i - 1] > 1) items.push('...')
    items.push(sorted[i])
  }
  return items
}

export default function Pagination({ page, totalPages, onPageChange }: PaginationProps) {
  if (totalPages <= 1) return null

  const items = getPageItems(page, totalPages)

  const btnBase =
    'inline-flex items-center justify-center min-w-[2rem] h-8 px-2 rounded text-sm font-medium transition-colors'
  const activeBtn = `${btnBase} bg-indigo-600 text-white`
  const inactiveBtn = `${btnBase} text-gray-600 hover:bg-gray-100`
  const disabledBtn = `${btnBase} text-gray-300 cursor-not-allowed`

  return (
    <div className="flex items-center justify-center gap-1 py-4">
      <button
        onClick={() => onPageChange(page - 1)}
        disabled={page === 1}
        className={page === 1 ? disabledBtn : inactiveBtn}
        aria-label="Previous page"
      >
        ←
      </button>

      {items.map((item, i) =>
        item === '...' ? (
          <span key={`ellipsis-${i}`} className="px-1 text-gray-400 text-sm select-none">
            …
          </span>
        ) : (
          <button
            key={item}
            onClick={() => onPageChange(item)}
            className={item === page ? activeBtn : inactiveBtn}
            aria-current={item === page ? 'page' : undefined}
          >
            {item}
          </button>
        ),
      )}

      <button
        onClick={() => onPageChange(page + 1)}
        disabled={page === totalPages}
        className={page === totalPages ? disabledBtn : inactiveBtn}
        aria-label="Next page"
      >
        →
      </button>
    </div>
  )
}
