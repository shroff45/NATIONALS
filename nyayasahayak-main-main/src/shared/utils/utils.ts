export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = error => reject(error);
    });
};

export const getLocalizedNumber = (num: number | string, locale = 'en-IN'): string => {
    const parsed = typeof num === 'string' ? parseFloat(num) : num;
    if (isNaN(parsed)) return String(num);
    return new Intl.NumberFormat(locale).format(parsed);
};
