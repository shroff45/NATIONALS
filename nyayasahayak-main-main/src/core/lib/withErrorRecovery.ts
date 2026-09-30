export const withErrorRecovery = async <T,>(
  fn: () => Promise<T>,
  fallback: T,
  options: { retryCount?: number } = {}
): Promise<T> => {
  try {
    return await fn();
  } catch (error) {
    console.warn("Error encountered, returning fallback", error);
    return fallback;
  }
};
