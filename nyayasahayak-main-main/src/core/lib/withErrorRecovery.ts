export const withErrorRecovery = async <T>(fn: () => Promise<T>, fallback?: any): Promise<T | null> => {
    try {
        return await fn();
    } catch (e) {
        console.error(e);
        return fallback || null;
    }
};
