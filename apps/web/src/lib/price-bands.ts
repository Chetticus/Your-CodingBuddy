/**
 * Shared by the server-rendered filter panel and the client radio group, so it
 * cannot live in a "use client" module.
 */
export const PRICE_BANDS = [
  { label: "Tất cả", min: "", max: "" },
  { label: "300.000 ₫", min: "300000", max: "300000" },
  { label: "400.000 ₫", min: "400000", max: "400000" },
  { label: "500.000 ₫", min: "500000", max: "500000" },
  { label: "Miễn phí", min: "0", max: "0" },
] as const;

export function bandIndex(min?: string, max?: string): number {
  const found = PRICE_BANDS.findIndex(
    (band) => band.min === (min ?? "") && band.max === (max ?? ""),
  );
  return found === -1 ? 0 : found;
}
