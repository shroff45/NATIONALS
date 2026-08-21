export const getLocalizedNumber = (num: number | string, language: string = 'en'): string => {
    const numStr = String(num);
    if (language === 'hi') {
        const hindiDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
        return numStr.replace(/[0-9]/g, w => hindiDigits[+w]);
    }
    return numStr;
};
