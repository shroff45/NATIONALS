export const withErrorRecovery = async <T>(fn: () => Promise<T>, fallbackResult?: T): Promise<T> => {
    try {
        return await fn();
    } catch (e) {
        console.error('Recovered error:', e);
        return fallbackResult as T;
    }
};
