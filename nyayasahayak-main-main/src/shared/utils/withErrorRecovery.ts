export const withErrorRecovery = async <T>(fn: () => Promise<T>, fallback?: T): Promise<T> => {
    try {
        return await fn();
    } catch (error) {
        console.error("Error occurred, attempting recovery...", error);
        if (fallback !== undefined) {
             return fallback;
        }
        throw error;
    }
};
