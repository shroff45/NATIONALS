export const withErrorRecovery = async <T,>(operation: () => Promise<T>, fallback: T): Promise<T> => {
    try {
        return await operation();
    } catch (error) {
        console.error("Error occurred, using fallback:", error);
        return fallback;
    }
};
