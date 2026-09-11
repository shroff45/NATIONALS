export function withErrorRecovery<T extends (...args: any[]) => Promise<any>>(
  fn: T,
  fallback?: Awaited<ReturnType<T>>
): T {
  return (async (...args: Parameters<T>) => {
    try {
      return await fn(...args);
    } catch (error) {
      console.error("Recovered from error:", error);
      return fallback;
    }
  }) as any;
}
