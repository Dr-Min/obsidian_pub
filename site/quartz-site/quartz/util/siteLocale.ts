import { QuartzPluginData } from "../plugins/vfile"
import { FullSlug, simplifySlug } from "./path"

export const SITE_LOCALES = ["ko", "en"] as const
export type SiteLocale = (typeof SITE_LOCALES)[number]

const LOCALE_NAMES: Record<SiteLocale, string> = {
  ko: "한국어",
  en: "English",
}

export function normalizeSiteLocale(value: unknown): SiteLocale | null {
  if (typeof value !== "string") {
    return null
  }

  const normalized = value.trim().toLowerCase()
  if (normalized.startsWith("ko")) {
    return "ko"
  }
  if (normalized.startsWith("en")) {
    return "en"
  }

  return null
}

export function getSiteLocaleName(locale: SiteLocale): string {
  return LOCALE_NAMES[locale]
}

export function localeFromSlug(slug?: string): SiteLocale | null {
  if (!slug) {
    return null
  }

  const [firstSegment] = slug.split("/")
  return normalizeSiteLocale(firstSegment)
}

export function localeFromPage(fileData: QuartzPluginData): SiteLocale | null {
  return normalizeSiteLocale(fileData.frontmatter?.lang) ?? localeFromSlug(fileData.slug)
}

export function stripLocaleSegment(slug?: string): string {
  if (!slug) {
    return ""
  }

  const segments = slug.split("/").filter(Boolean)
  if (segments.length === 0) {
    return ""
  }

  return normalizeSiteLocale(segments[0]) ? segments.slice(1).join("/") : segments.join("/")
}

export function translationGroupKey(fileData: QuartzPluginData): string | null {
  const explicitKey = fileData.frontmatter?.translationKey
  if (typeof explicitKey === "string" && explicitKey.trim().length > 0) {
    return explicitKey.trim()
  }

  const relativeSlug = stripLocaleSegment(fileData.slug)
  return relativeSlug || null
}

export function absoluteHrefForSlug(slug?: string): string | null {
  if (!slug) {
    return null
  }

  const simpleSlug = simplifySlug(slug as FullSlug)
  if (simpleSlug === "/") {
    return "/"
  }

  const normalized = String(simpleSlug).replace(/^\/+/, "")
  return `/${normalized}`
}

export function findLocalizedVariant(
  fileData: QuartzPluginData,
  allFiles: QuartzPluginData[],
  targetLocale: SiteLocale,
): QuartzPluginData | null {
  const currentLocale = localeFromPage(fileData)
  if (currentLocale === targetLocale) {
    return fileData
  }

  const groupKey = translationGroupKey(fileData)
  if (!groupKey) {
    return null
  }

  const translated = allFiles.find((candidate) => {
    return (
      candidate.slug !== fileData.slug &&
      localeFromPage(candidate) === targetLocale &&
      translationGroupKey(candidate) === groupKey
    )
  })
  if (translated) {
    return translated
  }

  const relativeSlug = stripLocaleSegment(fileData.slug)
  if (!relativeSlug) {
    return null
  }

  const fallbackSlug = `${targetLocale}/${relativeSlug}`
  return allFiles.find((candidate) => candidate.slug === fallbackSlug) ?? null
}

export function getAvailableLocales(
  fileData: QuartzPluginData,
  allFiles: QuartzPluginData[],
): SiteLocale[] {
  return SITE_LOCALES.filter((locale) => Boolean(findLocalizedVariant(fileData, allFiles, locale)))
}

export function isLocaleHome(fileData: QuartzPluginData): boolean {
  const relativeSlug = stripLocaleSegment(fileData.slug)
  return relativeSlug === "index"
}

export function localeHref(
  fileData: QuartzPluginData,
  allFiles: QuartzPluginData[],
  targetLocale: SiteLocale,
): string | null {
  const variant = findLocalizedVariant(fileData, allFiles, targetLocale)
  return absoluteHrefForSlug(variant?.slug)
}
