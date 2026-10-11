export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve((reader.result as string).split(',')[1]);
        reader.onerror = error => reject(error);
    });
};
export const getLocalizedNumber = (num: number | string, locale: string): string => {
    return new Intl.NumberFormat(locale).format(typeof num === "string" ? parseFloat(num) : num);
};
