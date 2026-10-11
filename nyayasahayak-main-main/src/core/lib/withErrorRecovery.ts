export async function withErrorRecovery<T>(
    operation: () => Promise<T>,
    fallbackMessage?: string | T
): Promise<T> {
    try {
        return await operation();
    } catch (error) {
        console.error("Operation failed:", error);
        if (fallbackMessage !== undefined) { return fallbackMessage as T; }
        throw error;
    }
}
