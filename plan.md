1. Modify `nyayasahayak-main-main/src/personas/judge/pages/OrdersHistory.tsx` using a node script.
   ```bash
   cat << 'JS_EOF' > update_script.js
   const fs = require('fs');
   const filepath = 'nyayasahayak-main-main/src/personas/judge/pages/OrdersHistory.tsx';
   let content = fs.readFileSync(filepath, 'utf8');

   // Import useMemo
   content = content.replace("import React, { useState } from 'react';", "import React, { useState, useMemo } from 'react';");

   // Wrap filteredOrders in useMemo
   const oldFiltered = `const filteredOrders = MOCK_ORDERS.filter(order => {
        const matchesSearch = order.caseTitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
            order.cnr.toLowerCase().includes(searchQuery.toLowerCase()) ||
            order.parties.toLowerCase().includes(searchQuery.toLowerCase());
        const matchesType = filterType === 'all' || order.orderType === filterType;
        const matchesStatus = filterStatus === 'all' || order.status === filterStatus;
        return matchesSearch && matchesType && matchesStatus;
    });`;

   const newFiltered = `// ⚡ Bolt Optimization: Memoize filtered array to prevent O(N) recalculation on every render
    const filteredOrders = useMemo(() => MOCK_ORDERS.filter(order => {
        const matchesSearch = order.caseTitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
            order.cnr.toLowerCase().includes(searchQuery.toLowerCase()) ||
            order.parties.toLowerCase().includes(searchQuery.toLowerCase());
        const matchesType = filterType === 'all' || order.orderType === filterType;
        const matchesStatus = filterStatus === 'all' || order.status === filterStatus;
        return matchesSearch && matchesType && matchesStatus;
    }), [searchQuery, filterType, filterStatus]);

    // ⚡ Bolt Optimization: Memoize static array counts to prevent redundant looping
    const stats = useMemo(() => ({
        published: MOCK_ORDERS.filter(o => o.status === 'Published').length,
        pending: MOCK_ORDERS.filter(o => o.status === 'Pending Review').length,
        archived: MOCK_ORDERS.filter(o => o.status === 'Archived').length
    }), []);`;

   content = content.replace(oldFiltered, newFiltered);

   // Replace inline stats
   content = content.replace(/{MOCK_ORDERS\.filter\(o => o\.status === 'Published'\)\.length}/g, '{stats.published}');
   content = content.replace(/{MOCK_ORDERS\.filter\(o => o\.status === 'Pending Review'\)\.length}/g, '{stats.pending}');
   content = content.replace(/{MOCK_ORDERS\.filter\(o => o\.status === 'Archived'\)\.length}/g, '{stats.archived}');

   fs.writeFileSync(filepath, content);
   JS_EOF
   node update_script.js
   rm update_script.js
   ```

2. Verify the changes applied successfully.
   ```bash
   git diff nyayasahayak-main-main/src/personas/judge/pages/OrdersHistory.tsx
   ```

3. Run verification checks.
   ```bash
   cd nyayasahayak-main-main && npm run lint && npm run build
   ```

4. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

5. Submit the PR using the `submit` tool with title `⚡ Bolt: Memoize expensive array operations in OrdersHistory` and description including What, Why, Impact, Measurement.
