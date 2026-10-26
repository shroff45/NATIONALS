
export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            const base64String = reader.result as string;
            resolve(base64String.split(',')[1]);
        };
        reader.onerror = error => reject(error);
    });
};

export const getLocalizedNumber = (num: number | string, locale: string = 'en-IN'): string => {
    return new Intl.NumberFormat(locale).format(Number(num));
};
