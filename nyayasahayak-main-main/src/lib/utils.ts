import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getLocalizedNumber(num: number | string, language: string = 'en') {
    if (language === 'hi') {
        const numStr = String(num);
        const hindiDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
        return numStr.replace(/[0-9]/g, (match) => hindiDigits[parseInt(match)]);
    }
    return String(num).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            if (typeof reader.result === 'string') {
                const base64String = reader.result.split(',')[1];
                resolve(base64String);
            } else {
                reject(new Error('Failed to read file as base64'));
            }
        };
        reader.onerror = error => reject(error);
    });
};
