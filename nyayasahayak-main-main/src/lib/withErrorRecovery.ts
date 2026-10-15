export async function withErrorRecovery<T>(operation: () => Promise<T>, fallback?: T): Promise<T> {
    try {
        return await operation();
    } catch (error) {
        console.error("Operation failed:", error);
        if (fallback !== undefined) return fallback;
        throw error;
    }
}
