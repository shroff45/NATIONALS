export async function withErrorRecovery<T>(fn: () => Promise<T>, fallback: T): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    console.error('Recovered from error:', error);
    return fallback;
  }
}
