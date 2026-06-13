import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function getLocalizedNumber(num: number | string, locale: string = 'en-IN'): string {
    return Number(num).toLocaleString(locale);
}
