import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/footer.scss"
import { version } from "../../package.json"
import { localeFromPage } from "../util/siteLocale"
import { i18n } from "../i18n"

type FooterLink = {
  text: string
  href: string
}

function linksForLocale(locale: string | null): FooterLink[] {
  if (locale === "ko") {
    return [
      { text: "소개", href: "/ko/about" },
      { text: "개인정보처리방침", href: "/ko/privacy" },
      { text: "문의", href: "/ko/contact" },
    ]
  }

  if (locale === "en") {
    return [
      { text: "About", href: "/en/about" },
      { text: "Privacy", href: "/en/privacy" },
      { text: "Contact", href: "/en/contact" },
    ]
  }

  return [
    { text: "한국어", href: "/ko/" },
    { text: "English", href: "/en/" },
  ]
}

const LocalizedFooter: QuartzComponent = ({ displayClass, cfg, fileData }: QuartzComponentProps) => {
  const year = new Date().getFullYear()
  const locale = localeFromPage(fileData)
  const links = linksForLocale(locale)

  return (
    <footer class={`${displayClass ?? ""}`}>
      <p>
        {i18n(cfg.locale).components.footer.createdWith}{" "}
        <a href="https://quartz.jzhao.xyz/">Quartz v{version}</a> · {year}
      </p>
      <ul>
        {links.map((link) => (
          <li>
            <a href={link.href}>{link.text}</a>
          </li>
        ))}
      </ul>
    </footer>
  )
}

LocalizedFooter.css = style

export default (() => LocalizedFooter) satisfies QuartzComponentConstructor
