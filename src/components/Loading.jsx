import "./Loading.css"

// Define the number of rows you want to show in the skeleton
const SKELETON_ROWS = 10;
// Define the column count (based on your 22-column table)
const COLUMN_COUNT = 22;

export default function Loading(){
// Array of undefined values to map over for rows
    const skeletonRows = Array(SKELETON_ROWS).fill(undefined);

    // Array of undefined values to map over for columns
    const skeletonCells = Array(COLUMN_COUNT).fill(undefined);

    return (
        // The skeleton must return a <tbody>, just like your BorderTrack component
        <tbody>
            {skeletonRows.map((_, rowIndex) => (
                <tr key={rowIndex} className="skeleton-row">
                    {skeletonCells.map((_, cellIndex) => (
                        <td key={cellIndex}>
                            {/* The core "placeholder" element */}
                            <div className="skeleton-placeholder" />
                        </td>
                    ))}
                </tr>
            ))}
        </tbody>
    );
}