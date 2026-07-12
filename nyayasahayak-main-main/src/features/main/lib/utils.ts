export function fileToBase64(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = error => reject(error);
    });
}

export function getLocalizedNumber(number: number, language: string): string {
    return new Intl.NumberFormat(language === 'en' ? 'en-IN' : language).format(number);
}
