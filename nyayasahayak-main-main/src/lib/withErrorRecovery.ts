export function withErrorRecovery<T extends (...args: any[]) => Promise<any>>(
  fn: T,
  fallback: Awaited<ReturnType<T>> | ((error: Error) => Promise<Awaited<ReturnType<T>>>)
): T {
  return (async (...args: Parameters<T>): Promise<Awaited<ReturnType<T>>> => {
    try {
      return await fn(...args);
    } catch (err) {
      console.error("Recovered from error:", err);
      return typeof fallback === 'function' ? await (fallback as any)(err) : fallback;
    }
  }) as T;
}
