export function withErrorRecovery<T extends (...args: any[]) => any>(fn: T): T {
    return (async (...args: any[]) => {
        try {
            return await fn(...args);
        } catch (error) {
            console.error(error);
            return null as any;
        }
    }) as T;
}
