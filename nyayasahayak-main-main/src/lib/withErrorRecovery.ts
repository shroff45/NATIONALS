export const withErrorRecovery = async <T>(
    operation: () => Promise<T>,
    fallback: T | (() => T) | (() => Promise<T>)
): Promise<T> => {
    try {
        return await operation();
    } catch (error) {
        console.error("Error executing operation:", error);
        if (typeof fallback === 'function') {
            return (fallback as any)();
        }
        return fallback;
    }
};
