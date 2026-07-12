export async function withErrorRecovery<T>(fn: () => Promise<T>): Promise<T> {
    try {
        return await fn();
    } catch (e) {
        console.error("Error during withErrorRecovery:", e);
        throw e;
    }
}
