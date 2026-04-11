import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import {
  SITE_LOCALES,
  absoluteHrefForSlug,
  getAvailableLocales,
  getSiteLocaleName,
  isLocaleHome,
  localeFromPage,
  localeHref,
} from "../util/siteLocale"

export default (() => {
  const LanguageSwitcher: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
  }: QuartzComponentProps) => {
    const currentLocale = localeFromPage(fileData)

    const links =
      fileData.slug === "index"
        ? SITE_LOCALES.map((locale) => ({
            locale,
            href: absoluteHrefForSlug(`${locale}/index`),
            active: false,
          }))
        : getAvailableLocales(fileData, allFiles).map((locale) => ({
            locale,
            href: localeHref(fileData, allFiles, locale),
            active: locale === currentLocale,
          }))

    const visibleLinks = links.filter((link) => Boolean(link.href))
    if (visibleLinks.length < 2 && !isLocaleHome(fileData)) {
      return null
    }

    return (
      <nav class={classNames(displayClass, "language-switcher")} aria-label="Language switcher">
        <span class="language-switcher-label">Language</span>
        <ul>
          {visibleLinks.map((link) => (
            <li>
              <a
                href={link.href!}
                hrefLang={link.locale}
                lang={link.locale}
                class={link.active ? "active" : undefined}
              >
                {getSiteLocaleName(link.locale)}
              </a>
            </li>
          ))}
        </ul>
      </nav>
    )
  }

  LanguageSwitcher.css = `
.language-switcher {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin: 0.75rem 0 1.25rem;
  flex-wrap: wrap;
}

.language-switcher-label {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--darkgray);
}

.language-switcher ul {
  display: flex;
  gap: 0.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
  flex-wrap: wrap;
}

.language-switcher a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.35rem 0.8rem;
  border: 1px solid var(--lightgray);
  border-radius: 999px;
  text-decoration: none;
  font-size: 0.95rem;
  color: var(--dark);
}

.language-switcher a.active {
  border-color: var(--secondary);
  background: var(--highlight);
  font-weight: 600;
}
`

  return LanguageSwitcher
}) satisfies QuartzComponentConstructor
