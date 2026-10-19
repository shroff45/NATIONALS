import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getLocalizedNumber(num: number | string, language: string = 'en'): string {
    const n = typeof num === 'string' ? parseFloat(num) : num;
    if (isNaN(n)) return String(num);

    switch (language) {
        case 'hi':
            return new Intl.NumberFormat('en-IN').format(n);
        case 'mr':
            return new Intl.NumberFormat('en-IN').format(n);
        default:
            return new Intl.NumberFormat('en-US').format(n);
    }
}
export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            if (typeof reader.result === 'string') {
                resolve(reader.result.split(',')[1]);
            } else {
                reject(new Error('Failed to convert file to base64'));
            }
        };
        reader.onerror = (error) => reject(error);
    });
};
