export const withErrorRecovery = async <T>(fn: () => Promise<T>, fallbackData?: T): Promise<T> => {
    try {
        return await fn();
    } catch (error) {
        console.error("Error occurred, attempting recovery...", error);
        if (fallbackData !== undefined) {
            return fallbackData;
        }
        throw error;
    }
};