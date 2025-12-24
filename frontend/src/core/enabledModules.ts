export const enabledModules = ["auth", "landingpages", "chatbot", "analytics", "integration"] as const;
export type EnabledModule = typeof enabledModules[number];
