import { enabledModules } from "./enabledModules";

type NavItem = { label: string; href: string; module: string };

const NAV_BY_MODULE: Record<string, NavItem[]> = {
  auth: [{ label: "Home", href: "/dashboard", module: "auth" }, { label: "Login", href: "/login", module: "auth" }],
  landingpages: [{ label: "Landings", href: "/dashboard/landings", module: "landingpages" }],
  chatbot: [{ label: "Chatbots", href: "/dashboard/chatbots", module: "chatbot" }],
  analytics: [{ label: "Analytics", href: "/dashboard/analytics", module: "analytics" }],
  integration: []
};

export function getNavItems(): NavItem[] {
  const items: NavItem[] = [];
  for (const m of enabledModules) {
    items.push(...(NAV_BY_MODULE[m] || []));
  }
  // Mantener Home primero si existe
  items.sort((a, b) => (a.href === "/dashboard" ? -1 : b.href === "/dashboard" ? 1 : 0));
  // Eliminar duplicados por href
  const seen = new Set<string>();
  return items.filter(i => (seen.has(i.href) ? false : (seen.add(i.href), true)));
}
