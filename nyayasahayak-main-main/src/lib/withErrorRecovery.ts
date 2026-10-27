export async function withErrorRecovery<T>(
    operation: () => Promise<T>,
    fallback?: T | (() => T | Promise<T>)
): Promise<T> {
    try {
        return await operation();
    } catch (error) {
        console.error('Operation failed, attempting recovery...', error);
        if (fallback !== undefined) {
            return typeof fallback === 'function' ? await (fallback as Function)() : fallback;
        }
        throw error;
    }
}
